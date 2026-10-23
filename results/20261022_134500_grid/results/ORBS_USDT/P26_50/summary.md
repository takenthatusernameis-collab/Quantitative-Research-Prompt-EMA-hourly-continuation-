# EMA Hourly Continuation — ORBS/USDT P26_50

**Symbol:** ORBS/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 968 |
| net_profit_factor | 0.3717 |
| net_win_rate | 0.3874 |
| gross_profit_factor | 0.8758 |
| gross_win_rate | 0.4277 |
| sharpe_ratio | -10.6011 |
| sortino_ratio | -4.6860 |
| max_drawdown | 0.9977 |
| cagr | -0.9106 |
| net_avg_win | 15.7363 |
| net_avg_loss | -26.7755 |
| avg_hold_time_bars | 5.2665 |
| exposure | 0.2317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
