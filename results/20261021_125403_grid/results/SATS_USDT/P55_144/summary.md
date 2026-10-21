# EMA Hourly Continuation — SATS/USDT P55_144

**Symbol:** SATS/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.6569 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.8344 |
| gross_win_rate | 0.4534 |
| sharpe_ratio | -2.3948 |
| sortino_ratio | -0.6078 |
| max_drawdown | 0.5307 |
| cagr | -0.2445 |
| net_avg_win | 67.3985 |
| net_avg_loss | -83.0077 |
| avg_hold_time_bars | 16.8727 |
| exposure | 0.2458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
