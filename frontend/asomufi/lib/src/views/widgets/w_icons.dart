import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class WIcons extends StatefulWidget {
  final String text, pathImage;
  final Function event;

  WIcons({Key key, this.text, this.pathImage, this.event}) : super(key: key);

  @override
  State<StatefulWidget> createState() =>
      _WIcons(text: this.text, pathImage: this.pathImage, event: this.event);
}

class _WIcons extends State<WIcons> {
  final String text, pathImage;
  final Function event;
  _WIcons({this.text, this.pathImage, this.event});

  @override
  Widget build(BuildContext context) {
    return IconButton(
      icon: new Image.asset(this.pathImage),
      onPressed: this.event,
      tooltip: this.text,
      iconSize: 32,
    );
  }
}
