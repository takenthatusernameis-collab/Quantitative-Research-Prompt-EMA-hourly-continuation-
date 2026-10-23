# EMA Hourly Continuation — XPR/USDT P55_200

**Symbol:** XPR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.4579 |
| net_win_rate | 0.4480 |
| gross_profit_factor | 0.7946 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -4.5749 |
| sortino_ratio | -1.3284 |
| max_drawdown | 0.8245 |
| cagr | -0.4874 |
| net_avg_win | 35.4100 |
| net_avg_loss | -62.7704 |
| avg_hold_time_bars | 15.2286 |
| exposure | 0.2997 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
