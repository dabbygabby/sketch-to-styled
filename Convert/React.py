import json

def compute_color(colorParameter):
    newFill = colorParameter
    color = "rgba(" + str(int(newFill["color"]["red"]*255)) + ", " + str(int(newFill["color"]["green"]*255)) + ", " + str(int(newFill["color"]["blue"]*255)) + ", " + str(int(newFill["color"]["alpha"]*255)) + ")"
    return color

def get_fills(fills):
    if fills != []:
        newFill = fills[0]
        if newFill["isEnabled"]:
            color = compute_color(newFill)
            return color
        else:
            return "null"
    else:
        return "null" 

def get_shadow(shadows):
    if shadows != []:
        newShadow = shadows[0]
        if newShadow["isEnabled"] == True:
            color = compute_color(newShadow)
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

def get_border_radius(points):
    try:
        corners = points[0]["cornerRadius"]
        return corners
    except:
        return 0

def get_border(borders):
    if borders != []:
        newBorder = borders[0]
        if newBorder["isEnabled"] == True:
            color = compute_color(newBorder)
            thickness= newBorder["thickness"]
            border = str(thickness) + "px solid " + color
            return border
        else:
            return "null"
    else:
        return "null"

def buildStyledComponent(style):
    with open('styledOutput/styled.jsx', 'w') as f:
        f.write("import React from 'react'\n")
        f.write("import styled from 'styled-components'\n")
        f.write("export const StyledSketch = () => {\n")
        f.write("return(<GeneratedStyledComponent/>)\n")
        f.write("}\n")
        f.write("const GeneratedStyledComponent=styled.div`\n")
        f.write(style)
        f.write("`")
    f.close()

def computeStyle(file):
    width = file["frame"]["width"]
    height = file["frame"]["height"]
    color = get_fills(file["style"]["fills"])
    border = get_border(file["style"]["borders"])
    borderRadius = get_border_radius(file["points"])
    shadow = get_shadow(file["style"]["shadows"])
    style = "background:" + color + ";\n" + "box-shadow:" + shadow + ";\n" + "width:" + str(width) + "px;\n" + "height:" + str(height) + "px;\n" + "border-radius:" + str(borderRadius) + "px;\n" + "border: " + str(border) + ";\n"
    return style

# def main 
currentFile = 'output/Rectangle.json' 

with open(currentFile) as f:
    file = json.load(f)
    style = computeStyle(file)
    buildStyledComponent(style)
    f.close()