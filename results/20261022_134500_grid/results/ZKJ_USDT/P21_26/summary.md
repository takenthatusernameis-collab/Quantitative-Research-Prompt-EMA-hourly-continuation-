# EMA Hourly Continuation — ZKJ/USDT P21_26

**Symbol:** ZKJ/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1411 |
| net_profit_factor | 0.1540 |
| net_win_rate | 0.2218 |
| gross_profit_factor | 0.5090 |
| gross_win_rate | 0.3402 |
| sharpe_ratio | -21.6457 |
| sortino_ratio | -12.6711 |
| max_drawdown | 1.0000 |
| cagr | -0.9991 |
| net_avg_win | 5.8157 |
| net_avg_loss | -10.7653 |
| avg_hold_time_bars | 2.6478 |
| exposure | 0.1698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
