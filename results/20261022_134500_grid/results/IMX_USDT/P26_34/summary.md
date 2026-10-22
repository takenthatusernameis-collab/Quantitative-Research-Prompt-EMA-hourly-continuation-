# EMA Hourly Continuation — IMX/USDT P26_34

**Symbol:** IMX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1047 |
| net_profit_factor | 0.2867 |
| net_win_rate | 0.4021 |
| gross_profit_factor | 0.7096 |
| gross_win_rate | 0.4374 |
| sharpe_ratio | -11.1519 |
| sortino_ratio | -5.1214 |
| max_drawdown | 0.9989 |
| cagr | -0.9313 |
| net_avg_win | 9.5359 |
| net_avg_loss | -22.3689 |
| avg_hold_time_bars | 2.2092 |
| exposure | 0.1047 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
