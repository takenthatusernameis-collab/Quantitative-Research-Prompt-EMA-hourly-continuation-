# EMA Hourly Continuation — CPOOL/USDT P55_89

**Symbol:** CPOOL/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.5094 |
| net_win_rate | 0.4318 |
| gross_profit_factor | 0.8082 |
| gross_win_rate | 0.4387 |
| sharpe_ratio | -6.5359 |
| sortino_ratio | -2.4526 |
| max_drawdown | 0.9549 |
| cagr | -0.7050 |
| net_avg_win | 31.9267 |
| net_avg_loss | -47.6252 |
| avg_hold_time_bars | 3.2674 |
| exposure | 0.1066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
