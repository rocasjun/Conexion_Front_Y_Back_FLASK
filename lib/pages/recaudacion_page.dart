import 'package:flutter/material.dart';
import 'package:dsm_cus11_recaudacion/models/predio_model.dart';
import 'package:dsm_cus11_recaudacion/models/recaudacion_model.dart';
import 'package:dsm_cus11_recaudacion/pages/detalle_page.dart';

import 'package:charts_flutter/flutter.dart' as charts;
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:intl/intl.dart';

class RecaudacionesPage extends StatefulWidget {
  final Predio predio;

  const RecaudacionesPage({required this.predio});

  @override
  _RecaudacionesPageState createState() => _RecaudacionesPageState();
}

class _RecaudacionesPageState extends State<RecaudacionesPage> {
  late DateTime selectedDate; // Almacena la fecha seleccionada por el usuario
  final DateFormat dateFormat = DateFormat('yyyy-MM'); // Formato de fecha

  @override
  void initState() {
    super.initState();
    selectedDate =
        DateTime.now(); // Inicializa la fecha seleccionada con la fecha actual
  }

  Future<List<Recaudacion>> getRecaudaciones(DateTime selectedDate) async {
    // Realiza la solicitud HTTP para obtener las recaudaciones del mes seleccionado
    final url = Uri.parse(
        "http://127.0.0.1:5000/api/recaudaciones/recaudacion-predio/${widget.predio.idPredio}?fecha=${dateFormat.format(selectedDate)}");

    final response = await http.get(
      url,
      headers: {'Accept': 'application/json'},
    );

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      final recaudaciones = data["recaudaciones"] as List<dynamic>;

      return recaudaciones.map((json) => Recaudacion.fromJson(json)).toList();
    } else {
      throw Exception("Failed to fetch recaudaciones");
    }
  }

  Future<void> _selectDate(BuildContext context) async {
    final DateTime? picked = await showDatePicker(
      context: context,
      initialDate:
          selectedDate, // Utiliza la fecha seleccionada actualmente como fecha inicial
      firstDate: DateTime(
          2000), // Fecha mínima permitida (puedes ajustarla según tus necesidades)
      lastDate:
          DateTime.now(), // Fecha máxima permitida (hasta la fecha actual)
      initialDatePickerMode:
          DatePickerMode.year, // Mostrar selector de año y mes
    );
    if (picked != null && picked != selectedDate) {
      setState(() {
        selectedDate = picked; // Actualiza la fecha seleccionada
      }); // HECHO EN LA PARTE DE ABAJO (IGNORAR)

      // Realiza la nueva solicitud HTTP con la fecha seleccionada
      //final recaudaciones = await getRecaudaciones(selectedDate);
      // Actualiza la interfaz con las nuevas recaudaciones
      // ...
    }
  }

  @override
  Widget build(BuildContext context) {
    NumberFormat numberFormat = NumberFormat("#,##0.00");
    // Create a function to handle the onTap event of the card

    return FutureBuilder<List<Recaudacion>>(
      future: getRecaudaciones(selectedDate),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return Center(child: CircularProgressIndicator());
        } else if (snapshot.hasError) {
          return Text('Error: ${snapshot.error}');
        } else if (snapshot.hasData) {
          final recaudaciones = snapshot.data!;

          void _navigateToDetailPage(Recaudacion recaudacion) {
            Navigator.push(
              context,
              MaterialPageRoute(
                  builder: (context) => DetailPage(recaudacion: recaudacion)),
            );
          }

          // Filtrar las recaudaciones por el mes específico seleccionado por el usuario
          final specificMonthRecaudaciones = recaudaciones.where((recaudacion) {
            final fecha = DateTime.parse(recaudacion.fechaOperacion);
            return fecha.month == selectedDate.month &&
                fecha.year == selectedDate.year;
          }).toList();

          // Crear una lista de widgets que muestre el nombre del inquilino y su recaudación
          final recaudacionesList =
              specificMonthRecaudaciones.map((recaudacion) {
            final inquilino = recaudacion
                .persona; //recaudacion.reciboMantRecaudacion.idMantRecibo
            final fecha = DateTime.parse(recaudacion.fechaOperacion);

            Color textColor = Colors.black; // Default color
            if (recaudacion.estadoRecaudacion.descripcion == "Validado") {
              //
              textColor = Colors
                  .green; // Green color if estado_recaudacion is "Validado"
            } else if (recaudacion.estadoRecaudacion.descripcion ==
                "Rechazado") {
              textColor =
                  Colors.red; // Red color if estado_recaudacion is "Rechazado"
            }

            return Card(
              child: IgnorePointer(
                ignoring:
                    recaudacion.estadoRecaudacion.descripcion != "Validado",
                child: InkWell(
                  onTap: () {
                    if (recaudacion.estadoRecaudacion.descripcion ==
                        "Validado") {
                      _navigateToDetailPage(
                          recaudacion); // Navigate to the detail page
                    }
                  },
                  child: ListTile(
                    title: Text(
                      'Inquilino: ${inquilino.nombres} ${inquilino.apellidoPaterno} ${inquilino.apellidoMaterno}',
                      style: TextStyle(color: textColor),
                    ),
                    subtitle: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          'Recaudación: ${recaudacion.importe}',
                          style: TextStyle(color: textColor),
                        ),
                        Text(
                          'Fecha: ${DateFormat('dd-MM-yyyy').format(fecha)}',
                          style: TextStyle(color: textColor),
                        ),
                        Text(
                          'ESTADO DE RECAUDACION: ${recaudacion.estadoRecaudacion.descripcion}',
                          style: TextStyle(color: textColor),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            );
          }).toList();

          // Filtrar las recaudaciones por el mes específico seleccionado por el usuario y por el estado "Validado"
          final validadoMonthRecaudaciones =
              specificMonthRecaudaciones.where((recaudacion) {
            final fecha = DateTime.parse(recaudacion.fechaOperacion);
            return fecha.month == selectedDate.month &&
                fecha.year == selectedDate.year &&
                recaudacion.estadoRecaudacion.descripcion == "Validado";
          }).toList();

          // Crear una serie de datos para el gráfico de barras
          final data = [
            charts.Series<Recaudacion, String>(
              id: 'recaudaciones',
              colorFn: (_, __) => charts.MaterialPalette.blue.shadeDefault,
              domainFn: (Recaudacion recaudacion, _) =>
                  recaudacion.fechaOperacion,
              measureFn: (Recaudacion recaudacion, _) =>
                  double.parse(recaudacion.importe),
              data: validadoMonthRecaudaciones,
              labelAccessorFn: (Recaudacion recaudacion, _) =>
                  '\$${recaudacion.importe}', // Display the exact number in the label
            ),
          ];

          final reciboMantData = [
            charts.Series<Recaudacion, String>(
              id: 'reciboMant',
              colorFn: (_, __) => charts.MaterialPalette.green.shadeDefault,
              domainFn: (_, __) => 'Recibo Mant.',
              measureFn: (Recaudacion recaudacion, _) =>
                  double.parse(recaudacion.reciboMantRecaudacion.importe),
              data: validadoMonthRecaudaciones,
              labelAccessorFn: (Recaudacion recaudacion, _) =>
                  '\$${recaudacion.reciboMantRecaudacion.importe}',
            ),
          ];

          final combinedData = List<charts.Series<dynamic, String>>.from(data)
            ..addAll(reciboMantData);

          final chart = charts.BarChart(
            combinedData.toList(),
            animate: true,
          );

          final totalRecaudado = validadoMonthRecaudaciones.fold(
              0.0,
              (total, recaudacion) =>
                  total + double.parse(recaudacion.importe));
          final totalReciboMant = validadoMonthRecaudaciones.fold(
              0.0,
              (total, recaudacion) =>
                  total +
                  double.parse(recaudacion.reciboMantRecaudacion.importe));
          final diferencia = totalReciboMant - totalRecaudado;

          final differenceBoxColor =
              diferencia == 0.0 ? Colors.green : Colors.red;

// Construir la vista
          return Scaffold(
            appBar: AppBar(
              title: Text('Recaudaciones - ${widget.predio.descripcion}'),
            ),
            body: Column(
              children: [
                Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text('Fecha seleccionada:'),
                      SizedBox(width: 8),
                      Text(dateFormat.format(
                          selectedDate)), // Muestra la fecha seleccionada
                      SizedBox(width: 8),
                      IconButton(
                        icon: Icon(Icons.calendar_today),
                        onPressed: () {
                          _selectDate(context); // Abre el selector de fecha
                        },
                      ),
                    ],
                  ),
                ),
                Expanded(
                  child: ListView(
                    children: recaudacionesList,
                  ),
                ),
                AspectRatio(
                  aspectRatio: 1.5, // Ajusta este valor a necesidad
                  child: Padding(
                    padding: EdgeInsets.all(16.0),
                    child: chart,
                  ),
                ),
                SizedBox(height: 16.0),
                Container(
                  padding: EdgeInsets.all(16.0),
                  decoration: BoxDecoration(
                    color: differenceBoxColor,
                    borderRadius: BorderRadius.circular(8.0),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        'Total Recibo del mes: $totalReciboMant',
                        style: TextStyle(color: Colors.white),
                      ),
                      Text(
                        'Total Recaudado: $totalRecaudado',
                        style: TextStyle(color: Colors.white),
                      ),
                      Text(
                        'Diferencia: ${numberFormat.format(diferencia)}',
                        style: TextStyle(color: Colors.white),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          );
        } else {
          return Center(child: Text('No se encontraron recaudaciones'));
        }
      },
    );
    //TODO FALTA AGREGAR LA BARRA DE NAVEGACION
  }
}

class BottomAppBarItem extends StatelessWidget {
  final IconData icon;
  final String title;

  const BottomAppBarItem({
    required this.icon,
    required this.title,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Icon(icon, color: Colors.white),
        SizedBox(height: 4),
        Text(
          title,
          style: TextStyle(color: Colors.white),
        ),
      ],
    );
  }
}
