# EMA Hourly Continuation — BLZ/USDT P21_144

**Symbol:** BLZ/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.5715 |
| net_win_rate | 0.4324 |
| gross_profit_factor | 0.8360 |
| gross_win_rate | 0.4378 |
| sharpe_ratio | -4.7078 |
| sortino_ratio | -1.5559 |
| max_drawdown | 0.8552 |
| cagr | -0.5243 |
| net_avg_win | 47.0330 |
| net_avg_loss | -62.7069 |
| avg_hold_time_bars | 22.3622 |
| exposure | 0.5617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
