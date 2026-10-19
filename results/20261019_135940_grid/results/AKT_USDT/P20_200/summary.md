# EMA Hourly Continuation — AKT/USDT P20_200

**Symbol:** AKT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.7511 |
| net_win_rate | 0.5058 |
| gross_profit_factor | 1.0414 |
| gross_win_rate | 0.5104 |
| sharpe_ratio | -1.8332 |
| sortino_ratio | -0.5371 |
| max_drawdown | 0.4954 |
| cagr | -0.2275 |
| net_avg_win | 65.7273 |
| net_avg_loss | -89.5564 |
| avg_hold_time_bars | 29.8938 |
| exposure | 0.5884 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
