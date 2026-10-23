# EMA Hourly Continuation — OGN/USDT P21_26

**Symbol:** OGN/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1150 |
| net_profit_factor | 0.2476 |
| net_win_rate | 0.3530 |
| gross_profit_factor | 0.7737 |
| gross_win_rate | 0.4226 |
| sharpe_ratio | -14.5352 |
| sortino_ratio | -7.1638 |
| max_drawdown | 0.9999 |
| cagr | -0.9790 |
| net_avg_win | 8.1055 |
| net_avg_loss | -17.8632 |
| avg_hold_time_bars | 2.4730 |
| exposure | 0.1287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
