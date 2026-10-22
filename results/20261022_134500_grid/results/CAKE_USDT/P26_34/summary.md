# EMA Hourly Continuation — CAKE/USDT P26_34

**Symbol:** CAKE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1071 |
| net_profit_factor | 0.1958 |
| net_win_rate | 0.3697 |
| gross_profit_factor | 0.8291 |
| gross_win_rate | 0.4398 |
| sharpe_ratio | -13.8907 |
| sortino_ratio | -6.6657 |
| max_drawdown | 0.9999 |
| cagr | -0.9718 |
| net_avg_win | 6.1461 |
| net_avg_loss | -18.4186 |
| avg_hold_time_bars | 2.2624 |
| exposure | 0.1101 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
