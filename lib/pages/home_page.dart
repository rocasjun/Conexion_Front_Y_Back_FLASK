import 'dart:convert';

import 'package:dsm_cus11_recaudacion/models/predio_model.dart';
import 'package:dsm_cus11_recaudacion/pages/recaudacion_page.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:dsm_cus11_recaudacion/core/utils/size_utils.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final url =
      Uri.parse("http://127.0.0.1:5000/api/predios"); //127.0.0.1 - 10.0.2.2

  Future<List<Predio>> getPredios() async {
    final response = await http.get(url);
    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      final List<dynamic> prediosJson = data['predios'] as List<dynamic>;
      return prediosJson.map((json) => Predio.fromJson(json)).toList();
    } else {
      throw Exception('Error al obtener los predios');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Color(0xFF123456),
        title: const Text('CONDOMINIOS CONDOSA'),
      ),
      body: Center(
        child: FutureBuilder<List<Predio>>(
          future: getPredios(),
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return CircularProgressIndicator();
            } else if (snapshot.hasError) {
              return Text('Error al obtener los predios');
            } else if (snapshot.hasData) {
              final predios = snapshot.data!;
              return ListView.builder(
                itemCount: predios.length,
                itemBuilder: (context, index) {
                  final predio = predios[index]; //inicio de CARD
                  return GestureDetector(
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) =>
                                RecaudacionesPage(predio: predio),
                          ),
                        );
                      },
                      child: Card(
                        //MODIFICADO CHILD: EN VES DE RETURN
                        clipBehavior: Clip.antiAlias,
                        elevation: 0,
                        margin: EdgeInsets.only(top: 9),
                        color: ColorConstant.whiteA700,
                        shape: RoundedRectangleBorder(
                          side: BorderSide(
                            color: ColorConstant.blue800,
                            width: getHorizontalSize(1),
                          ),
                          borderRadius: BorderRadius.circular(12),
                        ),
                        child: Container(
                          height: getVerticalSize(200), //modificado
                          width: getHorizontalSize(200),
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(12),
                            border: Border.all(
                              color: ColorConstant.blue800,
                              width: getHorizontalSize(1),
                            ),
                          ),
                          child: Stack(
                            alignment: Alignment.center,
                            children: [
                              Align(
                                alignment: Alignment.center,
                                child: Padding(
                                  padding: EdgeInsets.only(left: 6, right: 6),
                                  child: Column(
                                    mainAxisSize: MainAxisSize.min,
                                    crossAxisAlignment:
                                        CrossAxisAlignment.start,
                                    mainAxisAlignment: MainAxisAlignment.start,
                                    children: [
                                      Padding(
                                        padding: EdgeInsets.only(left: 4),
                                        child: Row(
                                          children: [
                                            Text(
                                              predio.tipoPredio
                                                  .nombrePredio, //NOMBRE DEL TIPO DE PREDIO
                                              overflow: TextOverflow.ellipsis,
                                              textAlign: TextAlign.left,
                                              style: TextStyle(
                                                fontWeight: FontWeight.bold,
                                                fontSize: 16,
                                              ),
                                            ),
                                            SizedBox(width: 8),
                                            Text(
                                              predio
                                                  .descripcion, //NOMBRE DEL PREDIO
                                              overflow: TextOverflow.ellipsis,
                                              textAlign: TextAlign.left,
                                              style: TextStyle(
                                                fontWeight: FontWeight.bold,
                                                fontSize: 16,
                                              ),
                                            ),
                                          ],
                                        ),
                                      ),
                                      Padding(
                                        padding: EdgeInsets.only(top: 2),
                                        child: Divider(
                                          height: 1,
                                          thickness: 1,
                                          color: ColorConstant.blue800,
                                        ),
                                      ),
                                      Padding(
                                        padding: EdgeInsets.only(top: 2),
                                        child: Divider(
                                          height: 1,
                                          thickness: 1,
                                          color: ColorConstant.blue800,
                                        ),
                                      ),
                                      Padding(
                                        padding: EdgeInsets.only(
                                            left: 4, top: 3, right: 3),
                                        child: Row(
                                          mainAxisAlignment:
                                              MainAxisAlignment.spaceBetween,
                                          crossAxisAlignment:
                                              CrossAxisAlignment.start,
                                          children: [
                                            Expanded(
                                              flex: 2,
                                              child: Column(
                                                crossAxisAlignment:
                                                    CrossAxisAlignment.start,
                                                children: [
                                                  Text(
                                                    "Dirección: ${predio.direccion}",
                                                    style:
                                                        TextStyle(fontSize: 12),
                                                  ),
                                                  Text(
                                                    "Ubigeo: ${predio.idUbigeo}",
                                                    style:
                                                        TextStyle(fontSize: 12),
                                                  ),
                                                  Text(
                                                    "Teléfono: ${predio.telefono}",
                                                    style:
                                                        TextStyle(fontSize: 12),
                                                  ),
                                                  Text(
                                                    "Correo: ${predio.correo}",
                                                    style:
                                                        TextStyle(fontSize: 12),
                                                  ),
                                                ],
                                              ),
                                            ),
                                            Expanded(
                                              flex: 3,
                                              child: Container(
                                                height: getVerticalSize(
                                                    120), //imagen vertical
                                                width: getHorizontalSize(50),
                                                decoration: BoxDecoration(
                                                  borderRadius:
                                                      BorderRadius.circular(9),
                                                  image: DecorationImage(
                                                    image: AssetImage(
                                                        'assets/images/img_image10.png'), // ruta de tu imagen, mejorar, hallar una forma de listar independientemente
                                                    fit: BoxFit.cover,
                                                  ),
                                                ),
                                              ),
                                            ),
                                          ],
                                        ),
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                      )
                      //FINAL DE CARD
                      );
                },
              );
            } else {
              return Text('No se encontraron predios');
            }
          },
        ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        backgroundColor: Color(0xFF000080),
        unselectedItemColor: Colors.black,
        selectedItemColor: Colors.black,
        items: [
          BottomNavigationBarItem(
            icon: Icon(
              Icons.home,
              color: Colors.black,
            ),
            label: 'Home',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.money, color: Colors.black),
            label: 'Deudas',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.report, color: Colors.black),
            label: 'Reportes',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.person, color: Colors.black),
            label: 'Usuarios',
          ),
        ],
      ),
    );
  }
}

class ColorConstant {
  static const blue800 = Color(0xFF123456);
  static const whiteA700 = Color(0xFFFFFFFF);
}

/*onTapColumncondomini(BuildContext context) { ENCONTRAR UNA MEJOR MANERA DE UTILIZAR RUTAS
    NavigatorService.pushNamed(
      AppRoutes.iphone14NineScreen,
    );
}*/

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
