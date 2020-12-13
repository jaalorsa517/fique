import 'dart:io';

import 'package:path_provider/path_provider.dart';
import 'package:sqflite/sqlite_api.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import 'tablessql.dart';

class DBProvider {
  Database _database;

  Future<Database> get database async {
    if (_database != null) return _database;
    _database = await initDB();
    return _database;
  }

  initDB() async {
    Directory documentsDirectory = await getApplicationDocumentsDirectory();
    String path = join(documentsDirectory.path, "fique.db");
    return await openDatabase(path, version: 1, onOpen: (db) {},
        onCreate: (db, int) async {
      return await db.execute(tables.values.join(" "));
    });
  }
}
