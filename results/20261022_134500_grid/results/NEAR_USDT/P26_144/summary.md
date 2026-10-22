# EMA Hourly Continuation — NEAR/USDT P26_144

**Symbol:** NEAR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.6904 |
| net_win_rate | 0.4809 |
| gross_profit_factor | 0.9552 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -2.6402 |
| sortino_ratio | -0.8044 |
| max_drawdown | 0.6359 |
| cagr | -0.3191 |
| net_avg_win | 61.0679 |
| net_avg_loss | -81.9327 |
| avg_hold_time_bars | 21.6404 |
| exposure | 0.4623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
