#####Gradient Shader
init: 
    transform gradient:
        shader "color.gradient"
        u_gradient_left (1.0,1.0,0.5,1.0)
        u_gradient_right (0.0,0.0,.5,0.0)
        easein_bounce 2 u_gradient_left (1.0,5.0,0.0,1.0)
        easein_bounce .5 u_gradient_left (1.0,5.0,11.0,1.0)
        ease 3 u_gradient_left (1.0,1.0,0.5,1.0)
        repeat

    transform flame:
        subpixel True
        shader "color.gradient"
        u_gradient_left (.9,.7,.7,1.0)
        u_gradient_right (1.0,1.0,1.0,1.0)