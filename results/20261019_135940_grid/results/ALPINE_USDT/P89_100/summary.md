# EMA Hourly Continuation — ALPINE/USDT P89_100

**Symbol:** ALPINE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.2731 |
| net_win_rate | 0.3552 |
| gross_profit_factor | 0.7153 |
| gross_win_rate | 0.4272 |
| sharpe_ratio | -9.8463 |
| sortino_ratio | -3.5245 |
| max_drawdown | 0.9903 |
| cagr | -0.8416 |
| net_avg_win | 17.1477 |
| net_avg_loss | -34.5768 |
| avg_hold_time_bars | 3.9165 |
| exposure | 0.1088 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
