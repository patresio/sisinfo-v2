from django.http import JsonResponse
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from bidding_procurement.models import Bidding, Material
from bidding_supplier.models import Supplier

@login_required
def global_search(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        # Search Biddings
        biddings = Bidding.objects.filter(
            Q(name__icontains=query) |
            Q(administrative_process__icontains=query) |
            Q(modality__icontains=query)
        )[:5]
        for b in biddings:
            results.append({
                'title': b.name or f"Licitação {b.id}",
                'type': 'Licitação',
                'url': b.get_absolute_url() if hasattr(b, 'get_absolute_url') else '#'
            })

        # Search Suppliers
        suppliers = Supplier.objects.filter(
            Q(trade_name__icontains=query) |
            Q(company_name__icontains=query) |
            Q(cnpj__icontains=query)
        )[:5]
        for s in suppliers:
            results.append({
                'title': s.trade_name or s.company_name,
                'type': 'Fornecedor',
                'url': reverse('suppliers:editar_fornecedor', args=[s.slug]) if hasattr(s, 'slug') else '#'
            })

        # Search Materials
        materials = Material.objects.filter(name__icontains=query)[:5]
        for m in materials:
            results.append({
                'title': m.name,
                'type': 'Material',
                'url': m.get_absolute_url() if hasattr(m, 'get_absolute_url') else '#'
            })

    return JsonResponse({'results': results})
