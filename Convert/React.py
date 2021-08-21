import json

def get_fills(fills):
    newFill = fills[0]
    if newFill["isEnabled"]:
        color = "rgba(" + str(int(newFill["color"]["red"]*255)) + ", " + str(int(newFill["color"]["green"]*255)) + ", " + str(int(newFill["color"]["blue"]*255)) + ", " + str(int(newFill["color"]["alpha"]*255)) + ")"
        return color

def get_shadow(shadows):
    if shadows != []:
        newShadow = shadows[0]
        if newShadow["isEnabled"] == True:
            color = "rgba(" + str(int(newShadow["color"]["red"]*255)) + ", " + str(int(newShadow["color"]["green"]*255)) + ", " + str(int(newShadow["color"]["blue"]*255)) + ", " + str(int(newShadow["color"]["alpha"]*255)) + ")"
            x = newShadow["offsetX"]
            y = newShadow["offsetY"]
            blurRadius = newShadow["blurRadius"]
            spread = newShadow["spread"]
            shadow = str(x) + "px " + str(y) + "px " + str(blurRadius) + "px " + str(spread) + "px " + color
            return shadow
        else:
            return "null"
    else:
        return "null"

def buildStyledComponent(style):
    with open('styled.jsx', 'a+') as f:
        f.write("import React from 'react'\n")
        f.write("import styled from 'styled-components'\n")
        f.write("export const StyledSketch = () => {\n")
        f.write("return(<GeneratedStyledComponent/>)\n")
        f.write("}\n")
        f.write("const GeneratedStyledComponent=styled.div`\n")
        f.write(style)
        f.write("`")
    f.close()

def get_border_radius(points):
    corners = points[0]["cornerRadius"]
    return corners

def get_border(borders):
    if borders != []:
        newBorder = borders[0]
        if newBorder["isEnabled"] == True:
            color = "rgba(" + str(int(newBorder["color"]["red"]*255)) + ", " + str(int(newBorder["color"]["green"]*255)) + ", " + str(int(newBorder["color"]["blue"]*255)) + ", " + str(int(newBorder["color"]["alpha"]*255)) + ")"
            thickness= newBorder["thickness"]
            border = str(thickness) + "px solid " + color
            return border
        else:
            return "null"
    else:
        return "null"

with open('../output/Rectangle.json') as f:
    file = json.load(f)
    border = get_border(file["style"]["borders"])
    width = file["frame"]["width"]
    height = file["frame"]["height"]
    color = get_fills(file["style"]["fills"])
    shadow = get_shadow(file["style"]["shadows"])
    borderRadius = get_border_radius(file["points"])
    style = "background:" + color + ";\n" + "box-shadow:" + shadow + ";\n" + "width:" + str(width) + "px;\n" + "height:" + str(height) + "px;\n" + "border-radius:" + str(borderRadius) + "px;\n" + "border: " + str(border) + ";\n"
    buildStyledComponent(style)