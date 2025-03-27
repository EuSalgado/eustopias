def wrap_paragraphs(text):
    paragraphs = text.strip().split("\n")  # Divide el texto en párrafos
    wrapped_paragraphs = [f"<p>{p.strip()}</p>" for p in paragraphs if p.strip()]
    return "\n".join(wrapped_paragraphs)

# Ejemplo de uso
texto = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam facilisis arcu id justo consectetur, sed viverra dui pretium. Maecenas eget fringilla purus, id posuere est. Integer venenatis elit a varius vestibulum. Phasellus commodo diam nec faucibus mollis. Proin facilisis lacinia justo ac finibus. Donec maximus ac est quis rhoncus. Donec justo felis, gravida id diam ut, faucibus dictum tortor. Quisque ac libero commodo, vulputate justo a, interdum orci. Fusce a massa dictum, imperdiet sem eu, scelerisque lacus. Proin fermentum posuere ante in accumsan. Integer vitae fringilla augue. Maecenas aliquet fermentum quam quis semper. In a tincidunt nibh. Ut sed lobortis risus. In aliquet tellus mauris, quis volutpat ipsum ullamcorper vitae. Sed porta risus efficitur felis cursus suscipit.

Fusce justo est, fermentum eget nunc sit amet, blandit luctus tellus. Integer laoreet tortor ut pretium dignissim. Suspendisse varius nulla a odio dapibus, non accumsan mauris malesuada. Phasellus placerat arcu ac elit cursus pulvinar. Duis enim orci, aliquet at sollicitudin vel, ultricies eget risus. Fusce gravida nulla a venenatis varius. Etiam sit amet lectus turpis. Sed venenatis, ipsum eget condimentum fringilla, magna dui lacinia ante, eget accumsan justo justo ut sem. Nulla varius dignissim est. Maecenas dapibus iaculis lacus. Phasellus feugiat rutrum posuere.

Nam vel feugiat ipsum, sed consectetur nisi. Nunc viverra, nulla vel mattis varius, justo erat scelerisque dui, id pellentesque arcu lectus vel tellus. Duis sit amet sem pretium, porttitor orci id, euismod ipsum. Aenean condimentum porta pulvinar. Praesent dolor velit, placerat sed nulla quis, consequat eleifend ex. Quisque a augue non tortor sodales vehicula non rutrum felis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec vel est eu dolor pulvinar elementum tincidunt ut est. Nullam non elit nisi. In hac habitasse platea dictumst. Aliquam sit amet lacinia purus.

Sed lobortis augue id ornare hendrerit. Donec congue, elit a cursus feugiat, ex justo aliquam diam, sit amet lobortis lectus est sed lorem. Morbi fringilla tempus lectus sit amet lacinia. Nunc porta arcu elementum, condimentum diam iaculis, tristique erat. In sagittis, quam at condimentum ultricies, lacus ante hendrerit velit, eu viverra ipsum nisl id nibh. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed maximus dui id ligula ornare rhoncus. Duis cursus posuere libero iaculis condimentum. Proin iaculis massa in pharetra molestie. Vivamus volutpat at massa finibus imperdiet. Praesent tincidunt vehicula sem. Maecenas quam ante, hendrerit sed purus vitae, aliquet faucibus purus. Quisque sit amet odio sollicitudin, auctor turpis ut, malesuada erat. Quisque vitae pharetra leo, id tincidunt sem. Integer ullamcorper augue non nisi elementum condimentum.

Vestibulum gravida consequat mi in fermentum. Morbi interdum odio magna. Nunc vehicula vestibulum tincidunt. In dictum dolor enim, vitae tempor dolor luctus in. Sed in lobortis ipsum. Mauris gravida metus sed elit consectetur, nec laoreet elit molestie. Pellentesque non ante aliquam, finibus nisi ac, ornare arcu. Proin a rhoncus nulla. Nullam congue urna sit amet commodo lacinia. Duis egestas vitae justo ac sollicitudin. Phasellus pharetra, dolor at venenatis pharetra, metus sapien gravida enim, nec feugiat sem mi a diam. Morbi libero odio, vehicula sit amet euismod non, volutpat pretium ligula. Morbi fringilla cursus justo nec vulputate. Fusce sollicitudin urna odio, sit amet vehicula nibh lacinia vel. Donec fringilla magna massa, vitae mattis erat volutpat gravida.
"""

resultado = wrap_paragraphs(texto)
print(resultado)
