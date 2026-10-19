# EMA Hourly Continuation — TRAC/USDT P12_55

**Symbol:** TRAC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 860 |
| net_profit_factor | 0.5624 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 0.8882 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -5.4521 |
| sortino_ratio | -2.2423 |
| max_drawdown | 0.9387 |
| cagr | -0.6610 |
| net_avg_win | 30.6915 |
| net_avg_loss | -45.4998 |
| avg_hold_time_bars | 9.2826 |
| exposure | 0.3629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
