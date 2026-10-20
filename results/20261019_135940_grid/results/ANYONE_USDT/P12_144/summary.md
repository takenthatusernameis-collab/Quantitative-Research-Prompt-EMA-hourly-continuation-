# EMA Hourly Continuation — ANYONE/USDT P12_144

**Symbol:** ANYONE/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.8171 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0010 |
| gross_win_rate | 0.5023 |
| sharpe_ratio | -1.3599 |
| sortino_ratio | -0.4240 |
| max_drawdown | 0.4391 |
| cagr | -0.1810 |
| net_avg_win | 75.4059 |
| net_avg_loss | -92.2883 |
| avg_hold_time_bars | 30.2558 |
| exposure | 0.6574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
