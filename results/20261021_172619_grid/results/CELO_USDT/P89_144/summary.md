# EMA Hourly Continuation — CELO/USDT P89_144

**Symbol:** CELO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.6917 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9334 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -2.0249 |
| sortino_ratio | -0.4863 |
| max_drawdown | 0.4610 |
| cagr | -0.2003 |
| net_avg_win | 71.0954 |
| net_avg_loss | -95.0983 |
| avg_hold_time_bars | 8.2473 |
| exposure | 0.1056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
