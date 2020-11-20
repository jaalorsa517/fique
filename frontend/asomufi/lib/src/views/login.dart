import 'package:flutter/material.dart';

class Login extends StatefulWidget {
  final String title;

  Login({Key key, this.title}) : super(key: key);

  @override
  _LoginState createState() => _LoginState();
}

class _LoginState extends State<Login> {
  @override
  Widget build(BuildContext context) {
    Size media = MediaQuery.of(context).size;

    return Scaffold(
      body: Center(
        child: Container(
          width: media.width,
          decoration: BoxDecoration(
              gradient: LinearGradient(
                  begin: Alignment.topCenter,
                  end: Alignment.bottomCenter,
                  colors: [
                Color.fromRGBO(134, 219, 212, 1),
                Colors.white,
              ])),
          child: Column(
            children: [
              Expanded(
                  child: Row(
                children: [],
              )),
              Expanded(
                  child: Column(
                children: [],
              ))
            ],
          ),
        ),
      ),
    );
  }
}
