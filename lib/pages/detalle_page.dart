import 'package:flutter/material.dart';
//import 'package:dsm_cus11_recaudacion/pages/recaudacion_page.dart';

import '../models/recaudacion_model.dart';

class DetailPage extends StatelessWidget {
  final Recaudacion recaudacion;

  const DetailPage({required this.recaudacion});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Detalle de Recaudación'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Inquilino: ${recaudacion.persona.nombres} ${recaudacion.persona.apellidoPaterno} ${recaudacion.persona.apellidoMaterno}',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 8),
            Text(
              'Fecha: ${recaudacion.fechaOperacion}',
              style: TextStyle(fontSize: 16),
            ),
            SizedBox(height: 8),
            Text(
              'Importe: ${recaudacion.importe}',
              style: TextStyle(fontSize: 16),
            ),
            SizedBox(height: 8),
            Text(
              'Estado de Recaudación: ${recaudacion.estadoRecaudacion.descripcion}',
              style: TextStyle(fontSize: 16),
            ),
            SizedBox(height: 16),
            Text(
              'Detalles adicionales:',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 8),
            Text(
              'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
              'Sed vestibulum urna at nibh varius aliquet. Nulla facilisi. '
              'Duis id ipsum sed mi feugiat tincidunt.',
              style: TextStyle(fontSize: 16),
            ),
            // Aquí puedes agregar más detalles específicos de la recaudación
          ],
        ),
      ),
    );
  }
}
