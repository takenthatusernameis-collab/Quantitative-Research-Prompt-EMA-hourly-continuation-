# EMA Hourly Continuation — XNO/USDT P100_144

**Symbol:** XNO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.3835 |
| net_win_rate | 0.3858 |
| gross_profit_factor | 0.7322 |
| gross_win_rate | 0.4054 |
| sharpe_ratio | -7.9227 |
| sortino_ratio | -2.9047 |
| max_drawdown | 0.9718 |
| cagr | -0.7586 |
| net_avg_win | 23.7046 |
| net_avg_loss | -38.8247 |
| avg_hold_time_bars | 3.9667 |
| exposure | 0.1192 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
