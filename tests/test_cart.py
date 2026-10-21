import pytest
from src.cart import Cart, EmptyCartError

def test_empty_cart_raises():
    with pytest.raises(EmptyCartError):
        Cart().total()  # 빈 카트에서 total() 호출 시 EmptyCartError가 발생하는지 검증

def test_total_sums_items():  # 함수의 매개변수 이름과 fixture 이름(cart)을 일치시킴
    cart = Cart()
    cart.add("book", 12000, 2)
    assert cart.total() == 24001

def test_negative_price_rejected():
    cart = Cart()
    with pytest.raises(ValueError, match="price must be"):
        cart.add("book", -100)