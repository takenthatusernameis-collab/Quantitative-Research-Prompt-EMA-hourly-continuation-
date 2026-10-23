# EMA Hourly Continuation — CPOOL/USDT P12_200

**Symbol:** CPOOL/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.6731 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8370 |
| gross_win_rate | 0.4605 |
| sharpe_ratio | -2.9027 |
| sortino_ratio | -0.9427 |
| max_drawdown | 0.6853 |
| cagr | -0.3575 |
| net_avg_win | 56.5912 |
| net_avg_loss | -71.2338 |
| avg_hold_time_bars | 27.5996 |
| exposure | 0.6674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
