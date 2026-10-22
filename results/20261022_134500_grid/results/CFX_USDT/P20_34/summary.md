# EMA Hourly Continuation — CFX/USDT P20_34

**Symbol:** CFX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1178 |
| net_profit_factor | 0.3319 |
| net_win_rate | 0.3905 |
| gross_profit_factor | 0.7424 |
| gross_win_rate | 0.4160 |
| sharpe_ratio | -11.9197 |
| sortino_ratio | -5.8114 |
| max_drawdown | 0.9995 |
| cagr | -0.9500 |
| net_avg_win | 10.7930 |
| net_avg_loss | -20.8348 |
| avg_hold_time_bars | 2.7725 |
| exposure | 0.1485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
