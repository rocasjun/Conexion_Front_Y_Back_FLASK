import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:intl/intl.dart';

import 'package:dsm_cus11_recaudacion/models/recaudacion_model.dart';
import 'package:dsm_cus11_recaudacion/models/detalle_model.dart';

class DetailPage extends StatefulWidget {
  final Recaudacion recaudacion;

  const DetailPage({required this.recaudacion});

  @override
  _DetailPageState createState() => _DetailPageState();
}

class _DetailPageState extends State<DetailPage> {
  List<Detalle> detalles = [];

  @override
  void initState() {
    super.initState();
    fetchDetalles();
  }

  Future<void> fetchDetalles() async {
    final url = Uri.parse(
        'http://127.0.0.1:5000/api/recibos/recibo-tipo-gasto/${widget.recaudacion.reciboMantRecaudacion.idMantRecibo}');
    final response = await http.get(url);

    if (response.statusCode == 200) {
      final List<dynamic> data = jsonDecode(response.body);
      final List<Detalle> fetchedDetalles =
          data.map((json) => Detalle.fromJson(json)).toList();

      setState(() {
        detalles = fetchedDetalles;
      });
    } else {
      throw Exception('Failed to fetch detalles');
    }
  }

  @override
  Widget build(BuildContext context) {
    NumberFormat numberFormat = NumberFormat("#,##0.00");
    final String sumaDetalles =
        numberFormat.format(Detalle.calcularSumaDetalles(detalles));
    final double totalRecaudado = double.parse(widget.recaudacion.importe);
    final String totalRecaudadoFormateado = numberFormat.format(totalRecaudado);
    double diferencia =
        (Detalle.calcularSumaDetalles(detalles) - totalRecaudado);

    String area = widget.recaudacion.reciboMantRecaudacion.casa.area;
    int numero =
        widget.recaudacion.reciboMantRecaudacion.casa.numero;
    double? participacion =
        widget.recaudacion.reciboMantRecaudacion.casa.participacion;
    int piso = widget.recaudacion.reciboMantRecaudacion.casa.piso;

    return Scaffold(
      appBar: AppBar(
        title: Text('Detalle de Recaudación'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Área: $area',style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
            Text('Número: $numero' ,style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
            Text('Participación: $participacion' ,style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
            Text('Piso: $piso' ,style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
            Text(
              'Inquilino: ${widget.recaudacion.persona.nombres} ${widget.recaudacion.persona.apellidoPaterno} ${widget.recaudacion.persona.apellidoMaterno}',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 8),
            Text(
              'Fecha: ${widget.recaudacion.fechaOperacion}',
              style: TextStyle(fontSize: 16),
            ),
            SizedBox(height: 8),
            Text(
              'Importe: ${(totalRecaudadoFormateado)}',
              style: TextStyle(fontSize: 16),
            ),
            SizedBox(height: 8),
            Text(
              'Estado de Recaudación: ${widget.recaudacion.estadoRecaudacion.descripcion}',
              style: TextStyle(fontSize: 16),
            ),
            SizedBox(height: 16),
            Text(
              'Detalles del Recibo:',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 8),
            Expanded(
              child: ListView.builder(
                itemCount: detalles.length,
                itemBuilder: (context, index) {
                  final detalle = detalles[index];
                  return ListTile(
                    title: Text(
                      detalle.descripcion,
                      style: TextStyle(fontSize: 16),
                    ),
                    subtitle: Text(
                      'Total Tipo Gasto: ${numberFormat.format(detalle.totalTipoGasto)}',
                      style: TextStyle(fontSize: 14),
                    ),
                  );
                },
              ),
            ),
            SizedBox(height: 16),
            Container(
              padding: EdgeInsets.all(16.0),
              decoration: BoxDecoration(
                color: Colors.green,
                borderRadius: BorderRadius.circular(8.0),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Total Recibo del mes',
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                    ),
                  ),
                  SizedBox(height: 8),
                  Text(
                    'Suma de detalles adicionales: ${sumaDetalles}',
                    style: TextStyle(
                      fontSize: 16,
                      color: Colors.white,
                    ),
                  ),
                ],
              ),
            ),
            SizedBox(height: 16),
            Container(
              padding: EdgeInsets.all(16.0),
              decoration: BoxDecoration(
                color: Colors.blue,
                borderRadius: BorderRadius.circular(8.0),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Total Recaudado',
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                    ),
                  ),
                  SizedBox(height: 8),
                  Text(
                    'Importe de la recaudación: ${numberFormat.format(totalRecaudado)}',
                    style: TextStyle(
                      fontSize: 16,
                      color: Colors.white,
                    ),
                  ),
                ],
              ),
            ),
            Container(
              decoration: BoxDecoration(
                color: diferencia == 0 ? Colors.green : Colors.red,
              ),
              child: Column(
                children: [
                  Text(
                    'Diferencia',
                    style: TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                    ),
                  ),
                  Text(
                    diferencia.toStringAsFixed(2),
                    style: TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
      //TODO FALTA AGREGAR LA BARRA DE NAVEGACION
    );
  }
}
