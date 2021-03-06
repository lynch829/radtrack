SDDS1
!# little-endian
&description text="sigma matrix--input: atto.ele  lattice: atto.lte", contents="sigma matrix", &end
&parameter name=Step, description="Simulation step", type=long, &end
&column name=s, units=m, description=Distance, type=double,  &end
&column name=ElementName, description="Element name", format_string=%10s, type=string,  &end
&column name=ElementOccurence, description="Occurence of element", format_string=%6ld, type=long,  &end
&column name=ElementType, description="Element-type name", format_string=%10s, type=string,  &end
&column name=s1, symbol="$gs$r$b1$n", units=m, description="sqrt(<x*x>)", type=double,  &end
&column name=s12, symbol="$gs$r$b12$n", units=m, description="<x*xp'>", type=double,  &end
&column name=s13, symbol="$gs$r$b13$n", units="m$a2$n", description="<x*y>", type=double,  &end
&column name=s14, symbol="$gs$r$b14$n", units=m, description="<x*y'>", type=double,  &end
&column name=s15, symbol="$gs$r$b15$n", units="m$a2$n", description="<x*s>", type=double,  &end
&column name=s16, symbol="$gs$r$b16$n", units=m, description="<x*delta>", type=double,  &end
&column name=s17, symbol="$gs$r$b17$n", units="m*s", description="<x*t>", type=double,  &end
&column name=s2, symbol="$gs$r$b2$n", description="sqrt(<x'*x'>)", type=double,  &end
&column name=s23, symbol="$gs$r$b23$n", units=m, description="<x'*y>", type=double,  &end
&column name=s24, symbol="$gs$r$b24$n", description="<x'*y'>", type=double,  &end
&column name=s25, symbol="$gs$r$b25$n", units=m, description="<x'*s>", type=double,  &end
&column name=s26, symbol="$gs$r$b26$n", description="<x'*delta>", type=double,  &end
&column name=s27, symbol="$gs$r$b27$n", units=s, description="<x'*t>", type=double,  &end
&column name=s3, symbol="$gs$r$b3$n", units=m, description="sqrt(<y*y>)", type=double,  &end
&column name=s34, symbol="$gs$r$b34$n", units=m, description="<y*y'>", type=double,  &end
&column name=s35, symbol="$gs$r$b35$n", units="m$a2$n", description="<y*s>", type=double,  &end
&column name=s36, symbol="$gs$r$b36$n", units=m, description="<y*delta>", type=double,  &end
&column name=s37, symbol="$gs$r$b37$n", units="m*s", description="<y*t>", type=double,  &end
&column name=s4, symbol="$gs$r$b4$n", description="sqrt(<y'*y')>", type=double,  &end
&column name=s45, symbol="$gs$r$b45$n", units=m, description="<y'*s>", type=double,  &end
&column name=s46, symbol="$gs$r$b46$n", description="<y'*delta>", type=double,  &end
&column name=s47, symbol="$gs$r$b47$n", units=s, description="<y'*t>", type=double,  &end
&column name=s5, symbol="$gs$r$b5$n", units=m, description="sqrt(<s*s>)", type=double,  &end
&column name=s56, symbol="$gs$r$b56$n", units=m, description="<s*delta>", type=double,  &end
&column name=s57, symbol="$gs$r$b57$n", units="m*s", description="<s*t>", type=double,  &end
&column name=s6, symbol="$gs$r$b6$n", description="sqrt(<delta*delta>)", type=double,  &end
&column name=s67, symbol="$gs$r$b67$n", units=s, description="<delta*t>", type=double,  &end
&column name=s7, symbol="$gs$r$b7$n", description="sqrt(<t*t>)", type=double,  &end
&column name=ma1, symbol="max$sb$ex$sb$e", units=m, description="maximum absolute value of x", type=double,  &end
&column name=ma2, symbol="max$sb$ex'$sb$e", description="maximum absolute value of x'", type=double,  &end
&column name=ma3, symbol="max$sb$ey$sb$e", units=m, description="maximum absolute value of y", type=double,  &end
&column name=ma4, symbol="max$sb$ey'$sb$e", description="maximum absolute value of y'", type=double,  &end
&column name=ma5, symbol="max$sb$e$gD$rs$sb$e", units=m, description="maximum absolute deviation of s", type=double,  &end
&column name=ma6, symbol="max$sb$e$gd$r$sb$e", description="maximum absolute value of delta", type=double,  &end
&column name=ma7, symbol="max$sb$e$gD$rt$sb$e", units=s, description="maximum absolute deviation of t", type=double,  &end
&column name=minimum1, symbol="x$bmin$n", units=m, type=double,  &end
&column name=minimum2, symbol="x'$bmin$n", units=m, type=double,  &end
&column name=minimum3, symbol="y$bmin$n", units=m, type=double,  &end
&column name=minimum4, symbol="y'$bmin$n", units=m, type=double,  &end
&column name=minimum5, symbol="$gD$rs$bmin$n", units=m, type=double,  &end
&column name=minimum6, symbol="$gd$r$bmin$n", units=m, type=double,  &end
&column name=minimum7, symbol="t$bmin$n", units=s, type=double,  &end
&column name=maximum1, symbol="x$bmax$n", units=m, type=double,  &end
&column name=maximum2, symbol="x'$bmax$n", units=m, type=double,  &end
&column name=maximum3, symbol="y$bmax$n", units=m, type=double,  &end
&column name=maximum4, symbol="y'$bmax$n", units=m, type=double,  &end
&column name=maximum5, symbol="$gD$rs$bmax$n", units=m, type=double,  &end
&column name=maximum6, symbol="$gd$r$bmax$n", units=m, type=double,  &end
&column name=maximum7, symbol="t$bmax$n", units=s, type=double,  &end
&column name=Sx, symbol="$gs$r$bx$n", units=m, description=sqrt(<(x-<x>)^2>), type=double,  &end
&column name=Sxp, symbol="$gs$r$bx'$n", description=sqrt(<(x'-<x'>)^2>), type=double,  &end
&column name=Sy, symbol="$gs$r$by$n", units=m, description=sqrt(<(y-<y>)^2>), type=double,  &end
&column name=Syp, symbol="$gs$r$by'$n", description=sqrt(<(y'-<y'>)^2>), type=double,  &end
&column name=Ss, symbol="$gs$r$bs$n", units=m, description=sqrt(<(s-<s>)^2>), type=double,  &end
&column name=Sdelta, symbol="$gs$bd$n$r", description=sqrt(<(delta-<delta>)^2>), type=double,  &end
&column name=St, symbol="$gs$r$bt$n", units=s, description=sqrt(<(t-<t>)^2>), type=double,  &end
&column name=ex, symbol="$ge$r$bx$n", units=m, description="geometric horizontal emittance", type=double,  &end
&column name=enx, symbol="$ge$r$bx,n$n", units=m, description="normalized horizontal emittance", type=double,  &end
&column name=ecx, symbol="$ge$r$bx,c$n", units=m, description="geometric horizontal emittance less dispersive contributions", type=double,  &end
&column name=ecnx, symbol="$ge$r$bx,cn$n", units=m, description="normalized horizontal emittance less dispersive contributions", type=double,  &end
&column name=ey, symbol="$ge$r$by$n", units=m, description="geometric vertical emittance", type=double,  &end
&column name=eny, symbol="$ge$r$by,n$n", units=m, description="normalized vertical emittance", type=double,  &end
&column name=ecy, symbol="$ge$r$by,c$n", units=m, description="geometric vertical emittance less dispersive contributions", type=double,  &end
&column name=ecny, symbol="$ge$r$by,cn$n", units=m, description="normalized vertical emittance less dispersive contributions", type=double,  &end
&column name=betaxBeam, symbol="$gb$r$bx,beam$n", units=m, description="betax for the beam, excluding dispersive contributions", type=double,  &end
&column name=alphaxBeam, symbol="$ga$r$bx,beam$n", description="alphax for the beam, excluding dispersive contributions", type=double,  &end
&column name=betayBeam, symbol="$gb$r$by,beam$n", units=m, description="betay for the beam, excluding dispersive contributions", type=double,  &end
&column name=alphayBeam, symbol="$ga$r$by,beam$n", description="alphay for the beam, excluding dispersive contributions", type=double,  &end
&data mode=binary, &end
	                 _BEG_      MARK"�:��:.?Nܑ
��<�|�a�=�/�bq�=��0( ��Ӈ.�o�N;/_)٧�H��� /?v�'��=�$�r��h���$n}=y]�`��(;iâ|Z�;R}���:.?����f��<�WW<n䩽c('�UZ!;��v/终Ҙ� /?��7x�u=��"2�2#��s���w�;�h㈵��>�[[%�;�'�B4�8<C��6?���ߎ2:$�Q�o�2=��<� G?�
	�Gf"?�O�.<G?5�m�h"?�>��?�;���4?�@EH�L=��<� G�Õ�qf"���KI�F�4��/�b"����P���;���4�W�O5�L��~i�#�F?�
	�Gf"?�O�.<G?5�m�h"?�>��?]A�J|�3?�@EH�L="�:��:.?H��� /?R}���:.?�Ҙ� /?�h㈵��>C��6?$�Q�o�2=H[�?w�F>	K���ư>H[�?w�F>	K���ư>�y�2w�F>��+��ư>�y�2w�F>��+��ư>-I  @�m{�yp�'���@��[�p�{�G�zt?   COL      ECOLD{��?�>������=Dc� ᗥ=�y.}u{���ڠ��q�]��@������P���u���f?hm�l����:�g`�ʹ=1�_���}=B�9�m�=��r���;|2>�?�	?"B��k�=�$�}}�=q��$�T��&�Ș�;k����?F��/�.�=M^4ǪE�=m�hu!�;t�����>���kؠ���Mh��p8<"�҈?��|�����0��2=�dbf�!
?�_ :"?�옾?���ne"?�"���?��8���3? w���L=�dbf�!
��Gخ-"��옾����"��&M����8���3�����#�L���S��
?�_ :"?Ha3?���ne"?�"���?<�ڢ3? w���L=D{��?�>u���f?|2>�?�	?k����?t�����>"�҈?��0��2=JC5��>>٫I�e}><�C��>����e}> �0CV#>�"}f�>^M�M�U#>��%f�>(j�66�?������|�[���A�?�;y����{�G�zt?   W0      WATCHD{��?�>������=Dc� ᗥ=�y.}u{���ڠ��q�]��@������P���u���f?hm�l����:�g`�ʹ=1�_���}=B�9�m�=��r���;|2>�?�	?"B��k�=�$�}}�=q��$�T��&�Ș�;k����?F��/�.�=M^4ǪE�=m�hu!�;t�����>���kؠ���Mh��p8<"�҈?��|�����0��2=�dbf�!
?�_ :"?�옾?���ne"?�"���?��8���3? w���L=�dbf�!
��Gخ-"��옾����"��&M����8���3�����#�L���S��
?�_ :"?Ha3?���ne"?�"���?<�ڢ3? w���L=D{��?�>u���f?|2>�?�	?k����?t�����>"�҈?��0��2=JC5��>>٫I�e}><�C��>����e}> �0CV#>�"}f�>^M�M�U#>��%f�>(j�66�?������|�[���A�?�;y�����Q����?   U2FINN      LSRMDLTRm���{ ?
b����>,;*񉥬=0,�̈́o�=�{�P�s=X�"�:t�=D(��$��;�pwV�_?��6��=��6�P��=2R�U�=�E�AU�=.�p<6I�;�z���?����]�>��%��!�=<�,��������;�d��J?L�i���=��c�.�=x��5-��;�X�����>��8���=k�>��p8<�Y�XL?C�nv��&<b��Z�2=�4V��F?|+*��)?Rp�׊#?�Pj�T#? ����?"���h? �׌ٳL=�4V��F��{bzf)�Rp�׊#��Q��j�"� �*i+��6��dh� `��L�
�W��?|+*��)?0Zj�0�"?�Pj�T#? ����?"���h? �׌ٳL=m���{ ?�pwV�_?�z���?�d��J?�X�����>�Y�XL?b��Z�2=iK<
��>p�y�a�>�+B���>!gu��`�>�nn}s#>��v�s��>w	 r#>�-�5���>�i�����?x��7还u����?�� �ؿ)\���(�?   M0       MATR
�r)(?�K����>��<)Ѳ=!�YX�*�=Kq�H@��=ffVA�s�=UF(c�;�pwV�_?H�]"\�=��6�P��=�#D�T�=�E�AU�=D���G�;�r
�O�?Kzw0�>�Jt��;�=�7!��2���w�C��;�d��J?��8N��=��c�.�=�h[5��;Of����>�̌yV��=?�lh�p8<�Y�XL?Z؂�Ӗ%</��T�2=����?|+*��)?�4~Z�$?�Pj�T#?  ���?"���h? `��L=������{bzf)��4~Z�$��Q��j�"� @��3��6��dh� �pޅ�L�u8
�{?|+*��)?/�� �$?�Pj�T#?  ���?"���h? `��L=
�r)(?�pwV�_?�r
�O�?�d��J?Of����>�Y�XL?/��T�2=jK<
��>q�y�a�>�+B���>"gu��`�>�nn}s#>��v�s��>x	 r#>�-�5���>H�h�s�?BJ��1%y#��?�Z�R޿)\���(�?   W1      WATCH
�r)(?�K����>��<)Ѳ=!�YX�*�=Kq�H@��=ffVA�s�=UF(c�;�pwV�_?H�]"\�=��6�P��=�#D�T�=�E�AU�=D���G�;�r
�O�?Kzw0�>�Jt��;�=�7!��2���w�C��;�d��J?��8N��=��c�.�=�h[5��;Of����>�̌yV��=?�lh�p8<�Y�XL?Z؂�Ӗ%</��T�2=����?|+*��)?�4~Z�$?�Pj�T#?  ���?"���h? `��L=������{bzf)��4~Z�$��Q��j�"� @��3��6��dh� �pޅ�L�u8
�{?|+*��)?/�� �$?�Pj�T#?  ���?"���h? `��L=
�r)(?�pwV�_?�r
�O�?�d��J?Of����>�Y�XL?/��T�2=jK<
��>q�y�a�>�+B���>"gu��`�>�nn}s#>��v�s��>x	 r#>�-�5���>H�h�s�?BJ��1%y#��?�Z�R޿�z�G��?   CAV      RFDF�R/V6�?w��tjD->fyûU����i��p�E�PQ*1�=1����{>�f�kK��;g$�g�_?�D=rEн�\�'�Z���a�PX��=�a�h�� >��$����;�UE+m/?7�K�>]�^�73����g�)�>��(4�q�Ţ�;OtP?�Q�-U��!&��z�>蔓�o:��� �Qw�>o0N��s�KѸ!�7<��=�VKt?���=c������2=^�k�!z)?�0ɬ �)?-�XCL?P?'�$�j?  ��n?�?W���? ��(0]M=^�k�!z)����R)�-�XCL�P?'�$�j� ���q���?W����  ��fL�#�U��(?�0ɬ �)?�Yօ��J?��B��h?  ��n?�1��*֑? ��(0]M=�R/V6�?g$�g�_?�UE+m/?Ţ�;OtP?� �Qw�>��=�VKt?����2=�?B��>�[���a�>'�@y�>�?^��a�>���_�#p>�~�(���>W�Zo	�F>V��ѐ°>���@���� �`��g�U�?��en���z�G��?   W2      WATCH�R/V6�?w��tjD->fyûU����i��p�E�PQ*1�=1����{>�f�kK��;g$�g�_?�D=rEн�\�'�Z���a�PX��=�a�h�� >��$����;�UE+m/?7�K�>]�^�73����g�)�>��(4�q�Ţ�;OtP?�Q�-U��!&��z�>蔓�o:��� �Qw�>o0N��s�KѸ!�7<��=�VKt?���=c������2=^�k�!z)?�0ɬ �)?-�XCL?P?'�$�j?  ��n?�?W���? ��(0]M=^�k�!z)����R)�-�XCL�P?'�$�j� ���q���?W����  ��fL�#�U��(?�0ɬ �)?�Yօ��J?��B��h?  ��n?�1��*֑? ��(0]M=�R/V6�?g$�g�_?�UE+m/?Ţ�;OtP?� �Qw�>��=�VKt?����2=�?B��>�[���a�>'�@y�>�?^��a�>���_�#p>�~�(���>W�Zo	�F>V��ѐ°>���@���� �`��g�U�?��en��u=
ףp�?   M1       MATR�%���i?�0^�2d?>��r&a�Āڽe�Pf��b�=r����>��Q��;g$�g�_?�V"�� ��\�'�Z����!�ͤ=�a�h�� >�Z)mo�;����-HT?�23^մ>�
>�Y�,O"�r�>zA%>�8��Ţ�;OtP?�DJ��
U��!&��z�>qӔ)����>��;���>��KT5�s���}�ύ8<��=�VKt?ܓi�� �N��*3=��,Y[f9?�0ɬ �)?�]++u�p?P?'�$�j? @�z�/?�?W���? @r#9XP=��,Y[f9����R)��]++u�p�P?'�$�j� �h�����?W����  �S�J�z�j�I7?�0ɬ �)?�����2o?��B��h? @�z�/?�1��*֑? @r#9XP=�%���i?g$�g�_?����-HT?Ţ�;OtP?>��;���>��=�VKt? �N��*3=�?B��>�[���a�>#�@y�>�?^��a�>u��_�#p>�~�(���>��Zo	�F>ն�ѐ°>9��|�!@��A((��X	�w�G@w+��ҮD�