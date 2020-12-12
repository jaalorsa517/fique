import 'package:asomufi/src/views/widgets/styles_fonts.dart';
import 'package:asomufi/src/views/widgets/w_icons.dart';
import 'package:asomufi/src/views/widgets/w_textBox.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

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
      body: Container(
          width: media.width,
          decoration: BoxDecoration(
              gradient: LinearGradient(
                  begin: Alignment.topCenter,
                  end: Alignment.bottomCenter,
                  colors: [
                Color.fromRGBO(134, 219, 212, 1),
                Colors.white,
              ])),
          child: Column(children: [
            Expanded(
                flex: 1,
                child: Padding(
                  padding: const EdgeInsets.only(top: 20),
                  child: Row(
                    children: [
                      Expanded(
                          flex: 1,
                          child: WIcons(
                            text: 'Regresar',
                            pathImage: 'assets/bt_salir.png',
                          )),
                      Expanded(
                          flex: 5,
                          child: Image(
                            image: AssetImage('assets/logo.png'),
                            height: 128,
                            width: 128,
                          )),
                      Expanded(
                          flex: 1,
                          child: WIcons(
                              text: 'Inicio',
                              pathImage: 'assets/bt_inicio.png'))
                    ],
                  ),
                )),
            Expanded(
              flex: 3,
              child: Padding(
                padding: const EdgeInsets.only(left: 20.0, right: 20),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceAround,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Stack(children: [
                      Text('Bienvenido',
                          style: GoogleFonts.bangers(
                              fontSize: 25,
                              fontWeight: FontWeight.w400,
                              // color: Color.fromRGBO(249, 241, 241, 1),
                              letterSpacing: 0.7,
                              foreground: Paint()
                                ..style = PaintingStyle.stroke
                                ..strokeWidth = 1
                                ..color = Colors.black54,
                              shadows: [
                                Shadow(
                                    offset: Offset(0, 4),
                                    blurRadius: 4,
                                    color: Color.fromRGBO(0, 0, 0, 0.25)),
                              ])),
                      Text('Bienvenido',
                          style: GoogleFonts.bangers(
                              fontSize: 25,
                              fontWeight: FontWeight.w400,
                              color: Color.fromRGBO(249, 241, 241, 1),
                              letterSpacing: 0.7,
                              shadows: [
                                Shadow(
                                    offset: Offset(0, 4),
                                    blurRadius: 4,
                                    color: Color.fromRGBO(0, 0, 0, 25))
                              ]))
                    ]),
                    Text('Ingrese los datos para iniciar sesión',
                        style: GoogleFonts.roboto(
                            fontWeight: FontWeight.w700,
                            fontSize: 16,
                            color: Color.fromRGBO(89, 89, 94, 1))),
                    WTextBox(label: 'NICKNAME').textBox(),
                    WTextBox(label: 'CONTRASEÑA').textBox(),
                    Center(
                      child: SizedBox(
                        width: 190,
                        height: 40,
                        child: RaisedButton(
                          child: Text('INGRESAR', style: styleForm),
                          onPressed: () {},
                          color: Color.fromRGBO(236, 236, 236, 1),
                          shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(10)),
                        ),
                      ),
                    )
                  ],
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.only(top: 50, bottom: 50),
              child: Flexible(
                flex: 1,
                child: InkWell(
                    child: Text(
                  'Has olvidado tu contraseña',
                  style: styleForm,
                )),
              ),
            )
          ])),
    );
  }
}
