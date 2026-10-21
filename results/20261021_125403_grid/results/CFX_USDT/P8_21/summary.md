# EMA Hourly Continuation — CFX/USDT P8_21

**Symbol:** CFX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.8368 |
| net_win_rate | 0.5356 |
| gross_profit_factor | 1.1526 |
| gross_win_rate | 0.5356 |
| sharpe_ratio | -1.2937 |
| sortino_ratio | -0.4267 |
| max_drawdown | 0.4226 |
| cagr | -0.1781 |
| net_avg_win | 71.7383 |
| net_avg_loss | -98.8883 |
| avg_hold_time_bars | 5.5838 |
| exposure | 0.1317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
