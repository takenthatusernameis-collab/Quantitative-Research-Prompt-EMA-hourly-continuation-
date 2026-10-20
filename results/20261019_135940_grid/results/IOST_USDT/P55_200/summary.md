# EMA Hourly Continuation — IOST/USDT P55_200

**Symbol:** IOST/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.7319 |
| net_win_rate | 0.5244 |
| gross_profit_factor | 1.1397 |
| gross_win_rate | 0.5366 |
| sharpe_ratio | -1.9304 |
| sortino_ratio | -0.5557 |
| max_drawdown | 0.5241 |
| cagr | -0.2313 |
| net_avg_win | 61.3833 |
| net_avg_loss | -92.4702 |
| avg_hold_time_bars | 18.5366 |
| exposure | 0.3455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
