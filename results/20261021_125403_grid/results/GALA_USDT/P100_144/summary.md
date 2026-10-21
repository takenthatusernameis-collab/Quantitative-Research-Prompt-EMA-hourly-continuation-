# EMA Hourly Continuation — GALA/USDT P100_144

**Symbol:** GALA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 229 |
| net_profit_factor | 0.7939 |
| net_win_rate | 0.5109 |
| gross_profit_factor | 1.0459 |
| gross_win_rate | 0.5109 |
| sharpe_ratio | -1.1052 |
| sortino_ratio | -0.2407 |
| max_drawdown | 0.2845 |
| cagr | -0.1047 |
| net_avg_win | 79.8302 |
| net_avg_loss | -105.0437 |
| avg_hold_time_bars | 7.2009 |
| exposure | 0.0750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
