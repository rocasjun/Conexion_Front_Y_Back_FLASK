class Detalle {
  final String descripcion;
  final double totalTipoGasto;

  Detalle({
    required this.descripcion,
    required this.totalTipoGasto,
  });

  factory Detalle.fromJson(Map<String, dynamic> json) {
    return Detalle(
      descripcion: json['descripcion'],
      totalTipoGasto: json['total_tipo_gasto'].toDouble(),
    );
  }

  static double calcularSumaDetalles(List<Detalle> detalles) {
    double suma = 0.0;
    for (final detalle in detalles) {
      suma += detalle.totalTipoGasto;
    }
    return suma;
  }
  
}