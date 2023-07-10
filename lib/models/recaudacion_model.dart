class Recaudacion {
  final Persona persona;
  final CuentaPredioRecaudacion cuentaPredioRecaudacion;
  final EstadoRecaudacion estadoRecaudacion;
  final String fechaOperacion;
  final int idRecaudacion;
  final String importe;
  final MonedaRecaudacion monedaRecaudacion;
  final String nOperacion;
  final String observacion;
  final ReciboMantRecaudacion reciboMantRecaudacion;

  Recaudacion({
    required this.persona,
    required this.cuentaPredioRecaudacion,
    required this.estadoRecaudacion,
    required this.fechaOperacion,
    required this.idRecaudacion,
    required this.importe,
    required this.monedaRecaudacion,
    required this.nOperacion,
    required this.observacion,
    required this.reciboMantRecaudacion,
  });

  factory Recaudacion.fromJson(Map<String, dynamic> json) {
    return Recaudacion(
      persona: Persona.fromJson(json['cuenta_origen_recaudacion']['persona']),
      cuentaPredioRecaudacion: CuentaPredioRecaudacion.fromJson(json['cuenta_predio_recaudacion']),
      estadoRecaudacion: EstadoRecaudacion.fromJson(json['estado_recaudacion']),
      fechaOperacion: json['fecha_operacion'],
      idRecaudacion: json['id_recaudacion'],
      importe: json['importe'],
      monedaRecaudacion: MonedaRecaudacion.fromJson(json['moneda_recaudacion']),
      nOperacion: json['n_operacion'],
      observacion: json['observacion'],
      reciboMantRecaudacion: ReciboMantRecaudacion.fromJson(json['recibo_mant_recaudacion']),
    );
  }
}

class CuentaPredioRecaudacion {
  final int ncuenta;

  CuentaPredioRecaudacion({
    required this.ncuenta,
  });

  factory CuentaPredioRecaudacion.fromJson(Map<String, dynamic> json) {
    return CuentaPredioRecaudacion(
      ncuenta: json['ncuenta'],
    );
  }
}

class EstadoRecaudacion {
  final String descripcion;

  EstadoRecaudacion({
    required this.descripcion,
  });

  factory EstadoRecaudacion.fromJson(Map<String, dynamic> json) {
    return EstadoRecaudacion(
      descripcion: json['descripcion'],
    );
  }
}

class MonedaRecaudacion {
  final String descripcion;
  final String etiqueta;
  final int idTipoMoneda;

  MonedaRecaudacion({
    required this.descripcion,
    required this.etiqueta,
    required this.idTipoMoneda,
  });

  factory MonedaRecaudacion.fromJson(Map<String, dynamic> json) {
    return MonedaRecaudacion(
      descripcion: json['descripcion'],
      etiqueta: json['etiqueta'],
      idTipoMoneda: json['id_tipo_moneda'],
    );
  }
}

class ReciboMantRecaudacion {
  final String ajuste;
  final Casa casa;
  final int idMantRecibo;
  final String importe;
  final String nRecibo;
  final String periodo;

  ReciboMantRecaudacion({
    required this.ajuste,
    required this.casa,
    required this.idMantRecibo,
    required this.importe,
    required this.nRecibo,
    required this.periodo,
  });

  factory ReciboMantRecaudacion.fromJson(Map<String, dynamic> json) {
    return ReciboMantRecaudacion(
      ajuste: json['ajuste'],
      casa: Casa.fromJson(json['casa']),
      idMantRecibo: json['id_mant_recibo'],
      importe: json['importe'],
      nRecibo: json['n_recibo'],
      periodo: json['periodo'],
    );
  }
}

class Casa {
  final String area;
  final int idCasa;
  final int numero;
  final double? participacion;
  final int piso;
  final PredioMdu predioMdu;

  Casa({
    required this.area,
    required this.idCasa,
    required this.numero,
    required this.participacion,
    required this.piso,
    required this.predioMdu,
  });

  factory Casa.fromJson(Map<String, dynamic> json) {
    return Casa(
      area: json['area'],
      idCasa: json['id_casa'],
      numero: json['numero'],
      participacion: double.tryParse(json['participacion'] ?? ''),
      piso: json['piso'],
      predioMdu: PredioMdu.fromJson(json['predio_mdu']),
    );
  }
}

class PredioMdu {
  final String descripcion;
  final String? direccion;
  final int idMdu;
  final int idPredio;
  final int idPredioMdu;
  final int? numero;

  PredioMdu({
    required this.descripcion,
    required this.direccion,
    required this.idMdu,
    required this.idPredio,
    required this.idPredioMdu,
    required this.numero,
  });

  factory PredioMdu.fromJson(Map<String, dynamic> json) {
    return PredioMdu(
      descripcion: json['descripcion'],
      direccion: json['direccion'],
      idMdu: json['id_mdu'],
      idPredio: json['id_predio'],
      idPredioMdu: json['id_predio_mdu'],
      numero: json['numero'],
    );
  }
}

class Persona {
  final String apellidoMaterno;
  final String apellidoPaterno;
  final String ndocumento;
  final String nombres;

  Persona({
    required this.apellidoMaterno,
    required this.apellidoPaterno,
    required this.ndocumento,
    required this.nombres,
  });

  factory Persona.fromJson(Map<String, dynamic> json) {
    return Persona(
      apellidoMaterno: json['apellido_materno'],
      apellidoPaterno: json['apellido_paterno'],
      ndocumento: json['ndocumento'],
      nombres: json['nombres'],
    );
  }
}
