# EMA Hourly Continuation — CAKE/USDT P34_50

**Symbol:** CAKE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 877 |
| net_profit_factor | 0.2529 |
| net_win_rate | 0.4059 |
| gross_profit_factor | 0.7219 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -10.5982 |
| sortino_ratio | -4.5074 |
| max_drawdown | 0.9971 |
| cagr | -0.9018 |
| net_avg_win | 9.4826 |
| net_avg_loss | -25.6168 |
| avg_hold_time_bars | 2.7457 |
| exposure | 0.1095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
