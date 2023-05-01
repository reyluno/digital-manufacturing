G90 ; Set to absolute positioning mode
G21 ; Set to millimeter units
G28 ; Home all axes
G1 X100 Y50 Z3.5 F500 ; Move to the starting point (X=0, Y=0, Z=0) at a feedrate of 1000mm/min
G92 X0 Y0 Z0 E0
G1 X30.0 Y0.0 Z0 E0.8; Move to vertex 1 of the triangle
G1 X-14.999999999999993 Y25.980762113533164 Z0 E0.8 ; Move to vertex 2 of the triangle
G1 X-15.000000000000014 Y-25.980762113533153 Z0 E0.8 ; Move to vertex 3 of the triangle
G1 X30.0 Y0.0 Z0 E0.8 ; Move back to vertex 1 of the triangle
G1 Z1.0 ; Move up to the next layer
G1 X29.926921507794727 Y2.0926942123237593 Z1.0 E0.8; Move to vertex 1 of the triangle
G1 X-16.775787104122397 Y24.871127176651253 Z1.0 E0.8 ; Move to vertex 2 of the triangle
G1 X-13.151134403672337 Y-26.963821388975006 Z1.0 E0.8 ; Move to vertex 3 of the triangle
G1 X29.926921507794727 Y2.0926942123237593 Z1.0 E0.8 ; Move back to vertex 1 of the triangle
G1 Z2.0 ; Move up to the next layer
G1 X29.70804206224711 Y4.175193028801963 Z2.0 E0.8; Move to vertex 1 of the triangle
G1 X-18.469844259769744 Y23.640322608201664 Z2.0 E0.8 ; Move to vertex 2 of the triangle
G1 X-11.238197802477377 Y-27.81551563700362 Z2.0 E0.8 ; Move to vertex 3 of the triangle
G1 X29.70804206224711 Y4.175193028801963 Z2.0 E0.8 ; Move back to vertex 1 of the triangle
G1 Z3.0 ; Move up to the next layer
G1 X29.34442802201417 Y6.237350724532781 Z3.0 E0.8; Move to vertex 1 of the triangle
G1 X-20.073918190765742 Y22.294344764321835 Z3.0 E0.8 ; Move to vertex 2 of the triangle
G1 X-9.27050983124844 Y-28.531695488854606 Z3.0 E0.8 ; Move to vertex 3 of the triangle
G1 X29.34442802201417 Y6.237350724532781 Z3.0 E0.8 ; Move back to vertex 1 of the triangle
G1 Z4.0 ; Move up to the next layer
G1 X28.837850878149567 Y8.269120674509974 Z4.0 E0.8; Move to vertex 1 of the triangle
G1 X-21.580194010159527 Y20.839751113769925 Z4.0 E0.8 ; Move to vertex 2 of the triangle
G1 X-7.257656867990049 Y-29.10887178827989 Z4.0 E0.8 ; Move to vertex 3 of the triangle
G1 X28.837850878149567 Y8.269120674509974 Z4.0 E0.8 ; Move back to vertex 1 of the triangle
G1 Z5.0 ; Move up to the next layer
G1 X28.190778623577252 Y10.260604299770062 Z5.0 E0.8; Move to vertex 1 of the triangle
G1 X-22.981333293569335 Y19.283628290596187 Z5.0 E0.8 ; Move to vertex 2 of the triangle
G1 X-5.209445330007927 Y-29.544232590366242 Z5.0 E0.8 ; Move to vertex 3 of the triangle
G1 X28.190778623577252 Y10.260604299770062 Z5.0 E0.8 ; Move back to vertex 1 of the triangle
G1 Z6.0 ; Move up to the next layer
G1 X27.406363729278027 Y12.202099292274005 Z6.0 E0.8; Move to vertex 1 of the triangle
G1 X-24.270509831248418 Y17.6335575687742 Z6.0 E0.8 ; Move to vertex 2 of the triangle
G1 X-3.1358538980296213 Y-29.8356568610482 Z6.0 E0.8 ; Move to vertex 3 of the triangle
G1 X27.406363729278027 Y12.202099292274005 Z6.0 E0.8 ; Move back to vertex 1 of the triangle
G1 Z7.0 ; Move up to the next layer
G1 X26.48842778576781 Y14.084146883576722 Z7.0 E0.8; Move to vertex 1 of the triangle
G1 X-25.441442884692776 Y15.897577926996156 Z7.0 E0.8 ; Move to vertex 2 of the triangle
G1 X-1.0469849010750476 Y-29.981724810572874 Z7.0 E0.8 ; Move to vertex 3 of the triangle
G1 X26.48842778576781 Y14.084146883576722 Z7.0 E0.8 ; Move back to vertex 1 of the triangle
G1 Z8.0 ; Move up to the next layer
G1 X25.44144288469278 Y15.897577926996147 Z8.0 E0.8; Move to vertex 1 of the triangle
G1 X-26.488427785767804 Y14.084146883576729 Z8.0 E0.8 ; Move to vertex 2 of the triangle
G1 X1.0469849010750139 Y-29.981724810572874 Z8.0 E0.8 ; Move to vertex 3 of the triangle
G1 X25.44144288469278 Y15.897577926996147 Z8.0 E0.8 ; Move back to vertex 1 of the triangle
G1 Z9.0 ; Move up to the next layer
G1 X24.270509831248425 Y17.633557568774194 Z9.0 E0.8; Move to vertex 1 of the triangle
G1 X-27.406363729278024 Y12.202099292274013 Z9.0 E0.8 ; Move to vertex 2 of the triangle
G1 X3.1358538980295894 Y-29.835656861048207 Z9.0 E0.8 ; Move to vertex 3 of the triangle
G1 X24.270509831248425 Y17.633557568774194 Z9.0 E0.8 ; Move back to vertex 1 of the triangle
G1 Z10.0 ; Move up to the next layer
G1 Z15
M2 ; End of program
