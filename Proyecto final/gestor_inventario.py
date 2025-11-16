#ALUMNOS Juan Blanco y Samuel Araujo

from typing import Optional
from inventario import Inventario
from ingredientes import CategoriaIngrediente
from gestor_ingredientes import GestorIngredientes

class GestorInventario:
    def __init__(self, inventario: Inventario, gestor_ingredientes: GestorIngredientes):
        self.inventario = inventario
        self.gestor_ingredientes = gestor_ingredientes
    
    def visualizar_todo(self):
        print("\n" + "="*60)
        print("               INVENTARIO COMPLETO")
        print("="*60)
        
        total_productos = 0
        total_cantidad = 0
        
        for categoria in CategoriaIngrediente:
            ingredientes_categoria = self.gestor_ingredientes.listar_por_categoria(categoria)
            existencias = self.inventario.listar_por_categoria(ingredientes_categoria, categoria)
            
            print(f"\n {categoria.value.upper()} ({len(existencias)} productos)")
            print("-" * 40)
            
            if existencias:
                for nombre, cantidad in existencias.items():
                    total_productos += 1
                    total_cantidad += cantidad
                    ingrediente = self.gestor_ingredientes.buscar_por_nombre(nombre)
                    tipo_info = f" - {ingrediente.tipo}" if ingrediente else ""
                    costo_info = f" - ${ingrediente.costo:.2f}" if ingrediente and ingrediente.costo > 0 else ""
                    estado = "✅ " if cantidad > 0 else " "
                    print(f"  {estado}{nombre}{tipo_info}{costo_info}: {cantidad} unidades")
            else:
                print("  No hay productos en esta categoría")
        
        print("\n" + "="*60)
        print(f"RESUMEN: {total_productos} productos, {total_cantidad} unidades totales")
        print("="*60)
    
    def buscar_existencia(self, nombre_ingrediente: str) -> Optional[int]:
        ingrediente = self.gestor_ingredientes.buscar_por_nombre(nombre_ingrediente)
        if ingrediente:  
            cantidad = self.inventario.verificar_existencia(ingrediente)
            print(f"\n🔍 Información de '{nombre_ingrediente}':")  
            print(f"   Categoría: {ingrediente.categoria.value}")  
            print(f"   Tipo: {ingrediente.tipo}")
            print(f"   ID: {ingrediente.id}")
            print(f"   Costo: ${ingrediente.costo:.2f}")
            print(f"   Existencia: {cantidad} unidades")
            return cantidad
        return None
    
    def listar_existencias_por_categoria(self, categoria: CategoriaIngrediente):
        ingredientes_categoria = self.gestor_ingredientes.listar_por_categoria(categoria)
        existencias = self.inventario.listar_por_categoria(ingredientes_categoria, categoria)
        
        print(f"\n INVENTARIO DE {categoria.value.upper()}")
        print("-" * 50)
        
        if existencias:
            total_cantidad = 0
            for nombre, cantidad in existencias.items():
                total_cantidad += cantidad
                ingrediente = self.gestor_ingredientes.buscar_por_nombre(nombre)
                tipo_info = f" ({ingrediente.tipo})" if ingrediente else ""
                costo_info = f" - ${ingrediente.costo:.2f}" if ingrediente and ingrediente.costo > 0 else ""
                estado = "✅ " if cantidad > 10 else "⚠️ " if cantidad > 0 else "❌ "
                print(f"  {estado}{nombre}{tipo_info}{costo_info}: {cantidad} unidades")
            
            print(f"\nTotal: {len(existencias)} productos, {total_cantidad} unidades")
        else:
            print("  No hay productos en esta categoría")
    
    def actualizar_existencia(self, nombre_ingrediente: str, nueva_cantidad: int) -> bool:
        ingrediente = self.gestor_ingredientes.buscar_por_nombre(nombre_ingrediente)
        if ingrediente:
            cantidad_anterior = self.inventario.verificar_existencia(ingrediente)
            self.inventario.actualizar_existencia(ingrediente, nueva_cantidad)
            print(f"✅ Existencia de '{ingrediente.nombre}' actualizada:")
            print(f"   Anterior: {cantidad_anterior} unidades")
            print(f"   Nueva: {nueva_cantidad} unidades")
            print(f"   Diferencia: {nueva_cantidad - cantidad_anterior:+d} unidades")
            return True
        else:
            print(f"❌ Ingrediente '{nombre_ingrediente}' no encontrado.")
            return False