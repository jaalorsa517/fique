import 'dart:convert';

import 'package:test/test.dart';
import 'package:asomufi/src/controller/sincronizacion/sincronizacion.dart';

void main() {
  test('Comprobar sincronizacion api', () async {
    var response = await getApi();
    print(utf8.decode(response.bodyBytes));
    expect(response.statusCode, 200);
  });
}
