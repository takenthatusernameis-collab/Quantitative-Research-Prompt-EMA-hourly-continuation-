# EMA Hourly Continuation — ZBCN/USDT P55_200

**Symbol:** ZBCN/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.9788 |
| net_win_rate | 0.5358 |
| gross_profit_factor | 1.1383 |
| gross_win_rate | 0.5358 |
| sharpe_ratio | -0.0681 |
| sortino_ratio | -0.0178 |
| max_drawdown | 0.2063 |
| cagr | -0.0141 |
| net_avg_win | 92.6994 |
| net_avg_loss | -109.3249 |
| avg_hold_time_bars | 18.8598 |
| exposure | 0.2801 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
