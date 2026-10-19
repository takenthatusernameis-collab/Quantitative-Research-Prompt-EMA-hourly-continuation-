# EMA Hourly Continuation — IMX/USDT P55_100

**Symbol:** IMX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.5473 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.8977 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -4.7395 |
| sortino_ratio | -1.6877 |
| max_drawdown | 0.8803 |
| cagr | -0.5639 |
| net_avg_win | 34.5297 |
| net_avg_loss | -56.7981 |
| avg_hold_time_bars | 4.5509 |
| exposure | 0.1334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
