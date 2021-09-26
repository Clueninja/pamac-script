
All_Objects system;

class All_Objects
{
  ArrayList<Particle> particles;
  //ArrayList<Membrane> membranes; // maybe
  float rad;
  All_Objects(float n_rad, int n_of_particles, boolean are_random){
    rad = n_rad;
    if (are_random){
      for(int i = 0; i<n_of_particles; i++){
        particles.add(new Particle(new PVector(random(-10,10), random(-10,10), 0), new PVector(random(-10,10), random(-10,10), 0), rad));
      }
    }
  }
  
  void check_collisions(boolean ignore){
    
    for (int i =0; i < particles.size() ; i++){
      
      
      PVector i_p= particles.get(i).pos;
      PVector i_v = particles.get(i).vel;
      particles.get(i).pos = new PVector(i_p.x % 480, i_p.y % 120, 0 );
      
      if (!ignore){
      
        for (int j =0; j < particles.size() ; j++){
          PVector j_p= particles.get(j).pos;
          PVector j_v= particles.get(j).vel;
          
          if (j!=i){
            
            if (i_p.dist(j_p)<rad*2){
              particles.get(i).vel.x = 10;
              particles.get(i).vel.y = -10;
            }
          }
          
        }
      }
    }
  }
  
  void update(){
    for (Particle particle : particles){
      particle.update();
    }
  }
  void display(){
    for (Particle particle : particles){
        particle.display();
     }
  }

}

class Particle
{
  PVector pos, vel;
  float rad;
  
  Particle(PVector n_pos, PVector n_vel, float n_rad){
    pos = n_pos;
    vel = n_vel;
    rad = n_rad;
  }
  void update(){
    pos.x += vel.x;
    pos.y += vel.y;
  }
  
  void display(){
    ellipse(pos.x, pos.y, rad, rad);
  }
}





void setup(){
  size(480,120);
  system = new All_Objects(10.0,10, true);
}

void draw(){
  system.check_collisions(true);
  system.update();
  system.display();
}
