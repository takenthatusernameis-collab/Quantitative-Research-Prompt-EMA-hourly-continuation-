# EMA Hourly Continuation — DCR/USDT P20_100

**Symbol:** DCR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 746 |
| net_profit_factor | 0.5175 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8260 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -5.1284 |
| sortino_ratio | -1.9595 |
| max_drawdown | 0.9145 |
| cagr | -0.6138 |
| net_avg_win | 28.5932 |
| net_avg_loss | -46.5255 |
| avg_hold_time_bars | 12.3485 |
| exposure | 0.4169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
