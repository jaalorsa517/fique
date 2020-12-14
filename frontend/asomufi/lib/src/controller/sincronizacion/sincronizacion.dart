import 'package:http/http.dart' as http;
import 'package:asomufi/src/controller/sincronizacion/configApi.dart';
import 'dart:convert';

Future<http.Response> getApi() async =>
    await http.get(urls['sincronizacion'], headers: {
      "Authorization": "Basic " +
          base64.encode(utf8.encode(login["user"] + ":" + login["password"]))
    });

void syncClientes(List<Map> response) async {}
