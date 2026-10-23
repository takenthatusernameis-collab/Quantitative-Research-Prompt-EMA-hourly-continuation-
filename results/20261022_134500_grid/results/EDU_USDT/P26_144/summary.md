# EMA Hourly Continuation — EDU/USDT P26_144

**Symbol:** EDU/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.6530 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.8897 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -3.0947 |
| sortino_ratio | -1.0122 |
| max_drawdown | 0.7102 |
| cagr | -0.3833 |
| net_avg_win | 51.9968 |
| net_avg_loss | -70.2580 |
| avg_hold_time_bars | 20.3327 |
| exposure | 0.5005 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
