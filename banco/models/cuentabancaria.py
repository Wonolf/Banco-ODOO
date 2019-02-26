from odoo import models, fields, api, _


class CuentaBanco(models.Model):
    _name = 'banco.cuentabanco'
    iban = fields.Char('Cod IBAN', required=True)
    saldo = fields.Integer('Saldo', required=True)
    cliente = fields.Many2one('banco.cliente', "Cliente")
    entidad = fields.Many2one('banco.entidad', 'Entidad Bancaria')
    fecha = fields.Date('Fecha Inicio', required=True)

    def name_get(self):
        res =[]
        for record in self:
            name = record.iban
            res.append((record.id, name))
        return res
