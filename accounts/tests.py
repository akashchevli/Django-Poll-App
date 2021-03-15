from django.test import TestCase

# Create your tests here.

products = Product.objects.all()
list_products = list(Product.objects.values())

size = len(list_products)
for i in range(size):
    list_products[i]['name'] = list_products[i]['name'].lower()

list_products = json.dumps(list_products, cls=DjangoJSONEncoder)

context = {
    'products': products,
    'list_products': list_products
}
return render(request, 'search_app/index.html', context)


<input type="text" id="search" class="form-control" placeholder="Type here to search..." />

<div id="box">
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Price</th>
      </tr>
    </thead>
    <tbody>
     {% for product in products %}
      <tr>
        <td>{{ product.name }}</td>
        <td>{{ product.price }}</td>
        <td><img src="{{ product.image.url }}"></td>
      </tr>
     {% endfor %}
    </tbody>
  </table>
</div>

<div class="container">
  <div class="row">
    <form>
      <div class="mb-3">
        <label for="exampleInputEmail1" class="form-label">Email address</label>
        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
        <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
      </div>
      <div class="mb-3">
        <label for="exampleInputPassword1" class="form-label">Password</label>
        <input type="password" class="form-control" id="exampleInputPassword1">
      </div>
      <div class="mb-3 form-check">
        <input type="radio" id="payment" name="payment" value="Online Payment" onclick="get_button()">
        <label for="payment">Online Payment</label><br>
      </div>
      <button type="submit" id="btn_payment" class="btn btn-primary" style="display: none;">Submit</button>
    </form>
  </div>
</div>




function get_button()
{
  alert("hello")
  var is_checked = $('#payment').prop('checked');
  $('#btn_payment').toggle(is_checked);
}
var data = "{{ list_products }}"
console.log(data)

var rdata = JSON.parse(data.replace(/&quot;/g, '"'))
console.log(rdata)

var input = document.getElementById('search')
console.log(input)

var filter_arr = []


input.addEventListener('keyup', (e)=>{
  box.innerHTML = ""
   filter_arr = rdata.filter(info=> info["name"].includes(e.target.value))

   console.log(filter_arr)

   if(filter_arr.length > 0)
   {
      filter_arr.map(info=>{
        box.innerHTML += `<tr>
                          <td>${info['name']}</td>
                          <td>${info['price']}</td>
                          <td><img src=media/${info['image']}></td>`
      })
   }
})
