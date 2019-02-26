from odoo import models, fields, api, _

class Movimientos(models.Model):
    _name = 'banco.movimientos'
    cod = fields.Char('Codigo Movimiento', required=True)
    fecha = fields.Date('Fecha Moviiento', required=False)
    cliente = fields.Many2one('banco.cliente', "Cliente", required=True)
    saldo = fields.Integer()
    cantidad = fields.Integer('Cantidad', required=True)
    resultado = fields.Integer()
    suma = fields.Integer(compute='suma')
    resta = fields.Integer(compute='resta')

    def name_get(self):
        res = []
        for record in self:
            name = record.cod
            res.append((record.id, name))
        return res

    def suma(self):
        self.resultado = self.saldo + self.cantidad

    def resta(self):
        self.resultado = self.saldo - self.cantidad
