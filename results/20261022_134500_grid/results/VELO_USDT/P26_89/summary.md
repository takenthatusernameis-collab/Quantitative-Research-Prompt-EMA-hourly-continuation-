# EMA Hourly Continuation — VELO/USDT P26_89

**Symbol:** VELO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 730 |
| net_profit_factor | 0.6939 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 1.0000 |
| gross_win_rate | 0.4959 |
| sharpe_ratio | -3.5301 |
| sortino_ratio | -1.3382 |
| max_drawdown | 0.8182 |
| cagr | -0.4761 |
| net_avg_win | 50.5410 |
| net_avg_loss | -70.8707 |
| avg_hold_time_bars | 9.3315 |
| exposure | 0.3096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
