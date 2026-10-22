# EMA Hourly Continuation — AVAX/USDT P21_55

**Symbol:** AVAX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 905 |
| net_profit_factor | 0.5419 |
| net_win_rate | 0.4442 |
| gross_profit_factor | 0.9576 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -7.4390 |
| sortino_ratio | -3.1471 |
| max_drawdown | 0.9807 |
| cagr | -0.7892 |
| net_avg_win | 28.8325 |
| net_avg_loss | -42.5253 |
| avg_hold_time_bars | 5.0453 |
| exposure | 0.2075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
