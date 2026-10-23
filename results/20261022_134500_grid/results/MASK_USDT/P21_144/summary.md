# EMA Hourly Continuation — MASK/USDT P21_144

**Symbol:** MASK/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.4575 |
| net_win_rate | 0.4228 |
| gross_profit_factor | 0.7375 |
| gross_win_rate | 0.4393 |
| sharpe_ratio | -5.2889 |
| sortino_ratio | -1.7377 |
| max_drawdown | 0.8832 |
| cagr | -0.5682 |
| net_avg_win | 32.2228 |
| net_avg_loss | -51.5850 |
| avg_hold_time_bars | 21.2482 |
| exposure | 0.5254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
