# EMA Hourly Continuation — TRAC/USDT P55_144

**Symbol:** TRAC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.8126 |
| net_win_rate | 0.5090 |
| gross_profit_factor | 1.0279 |
| gross_win_rate | 0.5090 |
| sharpe_ratio | -1.2328 |
| sortino_ratio | -0.3500 |
| max_drawdown | 0.3518 |
| cagr | -0.1494 |
| net_avg_win | 72.7678 |
| net_avg_loss | -92.8111 |
| avg_hold_time_bars | 11.4578 |
| exposure | 0.2036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
