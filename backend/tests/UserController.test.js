import chai from 'chai';
import chaiHttp from 'chai-http';
import server from '../index'; // Expressアプリのエントリポイントを指す

chai.should();

chai.use(chaiHttp);

describe('UserController', () => {
  describe('/GET users', () => {
    it('it should GET all the users', (done) => {
      chai.request(server)
          .get('/api/users')
          .end((err, res) => {
                res.should.have.status(200);
                res.body.should.be.a('array');
                done();
          });
    });
  });
});
