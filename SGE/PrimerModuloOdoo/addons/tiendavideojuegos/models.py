# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

# pylint: disable=missing-class-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=tow-few-public-methods
class Juego(models.Model):
    _name = 'juego'
    name = fields.Char(string="Nombre videojuego", required=True)
    precio = fields.Float('Precio', digits=(12, 2))
    consola_id = fields.Many2one('consola', String="Consola")   
    _sql_constraints = [('name', 'UNIQUE (name)',
                         'ya existe ese videojuego')]
    iva = fields.Float('I.V.A', digits=(12, 2), default=1.21)
    preciofinal = fields.Integer(string="Precio final con IVA", required=True)
    ventas_ids = fields.Many2many('ventas', 'juegos_ventas_rel', 'juego_id', 'ventas_id',
                                  'Ventas')


    @api.onchange('precio', 'iva')
    def _onchange_price(self):
        # set auto-changing field
        self.preciofinal = self.precio * self.iva
        # Can optionally return a warning and domains
        if self.iva != 1.21:
            return {
                'warning': {
                    'title': "Error",
                    'message': "Has modificado el campo IVA, escribe el valor del IVA actual",
                }
            }

class Ventas(models.Model):
    _name = 'ventas'
    fechaventa = fields.Date(string="Start Date")
    juegos_ids = fields.Many2many('juego', 'juegos_ventas_rel', 'ventas_id', 'juego_id',
                                  'Juegos')
    clientes_ids = fields.Many2many('cliente', 'clientes_ventas_rel', 'ventas_id', 'cliente_id',
                                  'Clientes')
    

class Persona(models.Model):
    _name = 'persona'
    dni = fields.Char(string="dni", required=True)

    


class Empleado(models.Model):
    _inherit = 'persona'
    _name = 'empleado'
    name = fields.Char(string="Nombre empleado", required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    provincia_id = fields.Many2one('provincia', string="Provincia")
    genero = fields.Char(string="Genero", required=True)
    _sql_constraints = [('name', 'UNIQUE (name)',
                         'ya existe ese empleado')]
    _sql_constraints = [('prueba9', "CHECK (genero = 'hombre')", 'Error: Solo masculino y femenino!')]

class Cliente(models.Model):
    _inherit = 'persona'
    _name = 'cliente'
    name = fields.Char(string="Nombre cliente", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    nombrecompleto = fields.Char(string="Nombre Completo", compute='_compute_name')
    edad = fields.Float('Edad', digits=(12, 1))
    provincia_id = fields.Many2one('provincia', string="Provincia")
    _sql_constraints = [('name', 'UNIQUE (name)',
                         'ya existe ese empleado')]
    ventas_ids = fields.Many2many('ventas', 'clientes_ventas_rel', 'cliente_id', 'ventas_id',
                                  'Ventas')

    @api.depends('name', 'apellidos')
    def _compute_name(self):    
        for record in self:        
            record.nombrecompleto = (str(record.name)) + ' ' +  (str(record.apellidos))  

    @api.constrains('edad')
    def _check_something(self):
        for record in self:
            if record.edad < 18:
                raise ValidationError("No puede registrarse si no es mayor de edad: %s" % record.edad)


class Consola(models.Model):
    _name = 'consola'
    name = fields.Char(string="Nombre Consola")
    juego_id = fields.One2many('juego',
                                'consola_id',
                                string="Juegos Asociados")
    precio = fields.Float('Precio', digits=(12, 2))

class Provincia(models.Model):
    _name = 'provincia'
    name = fields.Char(string="Nombre Provincia")
    empleado_id = fields.One2many('empleado', 'provincia_id', string="Empleados en la provincia")
    cliente_id = fields.One2many('cliente', 'provincia_id', string="Clientes en la provincia")





