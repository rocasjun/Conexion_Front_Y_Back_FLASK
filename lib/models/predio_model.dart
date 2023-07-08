
class Predio {
  int idPredio;
  String descripcion;
  String ruc;
  String telefono;
  String correo;
  String direccion;
  String idUbigeo;
  String url_imagen;
  TipoPredio tipoPredio;

  Predio({
    required this.idPredio,
    required this.descripcion,
    required this.ruc,
    required this.telefono,
    required this.correo,
    required this.direccion,
    required this.idUbigeo,
    required this.url_imagen,
    required this.tipoPredio,
  });

  factory Predio.fromJson(Map<String, dynamic> json) {
    return Predio(
      idPredio: json['id_predio'],
      descripcion: json['descripcion'],
      ruc: json['ruc'],
      telefono: json['telefono'],
      correo: json['correo'],
      direccion: json['direccion'],
      idUbigeo: json['idubigeo'] != null ? json['idubigeo'] : '',
      url_imagen: json['url_imagen'] != null ? json['url_imagen'] : '', // Asigna un valor predeterminado en caso de que sea nulo
      tipoPredio: TipoPredio.fromJson(json['tipo_predio']),
    );
  }
}

class TipoPredio {
  String nombrePredio;

  TipoPredio({
    required this.nombrePredio,
  });

  factory TipoPredio.fromJson(Map<String, dynamic> json) {
    return TipoPredio(
      nombrePredio: json['nomre_predio'],
    );
  }
}
/*
class PredioService {
  static Future<List<Predio>> obtenerPredios() async {
    final response = await http.get(Uri.parse('http://127.0.0.1:5000/api/predios'));
    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      final List<dynamic> prediosJson = data['predios'] as List<dynamic>;
      return prediosJson.map((json) => Predio.fromJson(json)).toList();
    } else {
      throw Exception('Error al obtener los predios');
    }
  }
}*/
