import 'package:asomufi/src/views/widgets/styles_fonts.dart';
import 'package:flutter/material.dart';

class WTextBox {
  final String label;
  WTextBox({this.label});

  Widget textBox() {
    return Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      Text(this.label, style: styleForm),
      Container(
        child: TextField(
            decoration: InputDecoration(
                border: OutlineInputBorder(
                    borderRadius: BorderRadius.all(Radius.circular(10))),
                fillColor: Color.fromRGBO(236, 236, 236, 1),
                filled: true)),
        decoration: BoxDecoration(boxShadow: [
          BoxShadow(
              offset: const Offset(0, 4),
              blurRadius: 4,
              color: Color.fromRGBO(7, 7, 7, 0.457))
        ]),
      )
    ]);
  }
}
