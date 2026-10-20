# EMA Hourly Continuation — MINA/USDT P55_100

**Symbol:** MINA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.4926 |
| net_win_rate | 0.4315 |
| gross_profit_factor | 0.8493 |
| gross_win_rate | 0.4441 |
| sharpe_ratio | -6.0091 |
| sortino_ratio | -2.1393 |
| max_drawdown | 0.9305 |
| cagr | -0.6474 |
| net_avg_win | 32.8459 |
| net_avg_loss | -50.6095 |
| avg_hold_time_bars | 5.6551 |
| exposure | 0.1632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
