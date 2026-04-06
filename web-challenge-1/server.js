import express from "express";

const app = express();

app.use(express.json());
app.use(express.urlencoded({extended: true}));

app.post('/api/purchase', (req, res) => {
  console.log(req.body)
  const { wallet, ...cart} = req.body;
  let totalPrice = 0;
  let isFlag = false;

  Object.values(cart).forEach(item => {
    if (item.name == 'Flag') {
      isFlag = true;
    }
    totalPrice += item.price;
  });

  if (wallet > totalPrice && isFlag) {
    res.send({success: 'Congratulations! Here is your flag: e2c713091377159ac0b73bb39c129f0dda2f59e2'});
    return ;
  }
  if (wallet > totalPrice && !isFlag) {
    res.send({success: 'We are sorry, we could not proceed with your request at this moment'})
    return ;
  }
  res.send({success: 'Could not process payment: not enough credit!'})
})
app.listen(5000, () => {
  console.log("[server] listening on port 5000");
});