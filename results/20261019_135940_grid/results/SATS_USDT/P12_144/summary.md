# EMA Hourly Continuation — SATS/USDT P12_144

**Symbol:** SATS/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.6125 |
| net_win_rate | 0.4458 |
| gross_profit_factor | 0.8474 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -3.4489 |
| sortino_ratio | -1.0900 |
| max_drawdown | 0.7320 |
| cagr | -0.4008 |
| net_avg_win | 50.7323 |
| net_avg_loss | -66.6141 |
| avg_hold_time_bars | 27.9172 |
| exposure | 0.6405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
