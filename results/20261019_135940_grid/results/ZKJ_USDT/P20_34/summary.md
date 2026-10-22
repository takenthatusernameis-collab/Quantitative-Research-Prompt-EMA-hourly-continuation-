# EMA Hourly Continuation — ZKJ/USDT P20_34

**Symbol:** ZKJ/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1374 |
| net_profit_factor | 0.1506 |
| net_win_rate | 0.2569 |
| gross_profit_factor | 0.4395 |
| gross_win_rate | 0.3501 |
| sharpe_ratio | -19.3312 |
| sortino_ratio | -10.7374 |
| max_drawdown | 1.0000 |
| cagr | -0.9973 |
| net_avg_win | 5.0221 |
| net_avg_loss | -11.5306 |
| avg_hold_time_bars | 3.5204 |
| exposure | 0.2199 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
