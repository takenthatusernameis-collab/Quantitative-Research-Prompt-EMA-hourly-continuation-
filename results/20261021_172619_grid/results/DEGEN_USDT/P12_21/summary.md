# EMA Hourly Continuation — DEGEN/USDT P12_21

**Symbol:** DEGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.7435 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9628 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -1.8128 |
| sortino_ratio | -0.4847 |
| max_drawdown | 0.4344 |
| cagr | -0.2003 |
| net_avg_win | 72.7493 |
| net_avg_loss | -93.9933 |
| avg_hold_time_bars | 5.9456 |
| exposure | 0.0945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
