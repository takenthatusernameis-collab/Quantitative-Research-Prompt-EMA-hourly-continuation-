# EMA Hourly Continuation — DOT/USDT P26_200

**Symbol:** DOT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.6501 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 0.9241 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -2.4228 |
| sortino_ratio | -0.6255 |
| max_drawdown | 0.5489 |
| cagr | -0.2595 |
| net_avg_win | 61.1275 |
| net_avg_loss | -86.0149 |
| avg_hold_time_bars | 39.6795 |
| exposure | 0.6078 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
