# EMA Hourly Continuation — DEGEN/USDT P26_50

**Symbol:** DEGEN/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 902 |
| net_profit_factor | 0.5521 |
| net_win_rate | 0.4246 |
| gross_profit_factor | 0.8426 |
| gross_win_rate | 0.4401 |
| sharpe_ratio | -7.1413 |
| sortino_ratio | -3.0254 |
| max_drawdown | 0.9756 |
| cagr | -0.7701 |
| net_avg_win | 31.3746 |
| net_avg_loss | -41.9378 |
| avg_hold_time_bars | 3.8803 |
| exposure | 0.1594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
