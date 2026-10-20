# EMA Hourly Continuation — GLM/USDT P50_89

**Symbol:** GLM/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 647 |
| net_profit_factor | 0.4248 |
| net_win_rate | 0.4405 |
| gross_profit_factor | 0.7965 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -5.9655 |
| sortino_ratio | -2.1545 |
| max_drawdown | 0.9266 |
| cagr | -0.6453 |
| net_avg_win | 23.9932 |
| net_avg_loss | -44.4681 |
| avg_hold_time_bars | 5.1097 |
| exposure | 0.1503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
