# EMA Hourly Continuation — POL/USDT P20_26

**Symbol:** POL/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 180 |
| net_profit_factor | 0.5200 |
| net_win_rate | 0.4222 |
| gross_profit_factor | 0.7371 |
| gross_win_rate | 0.4222 |
| sharpe_ratio | -2.7203 |
| sortino_ratio | -0.5200 |
| max_drawdown | 0.4757 |
| cagr | -0.2131 |
| net_avg_win | 64.4469 |
| net_avg_loss | -90.5736 |
| avg_hold_time_bars | 5.0500 |
| exposure | 0.0413 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
