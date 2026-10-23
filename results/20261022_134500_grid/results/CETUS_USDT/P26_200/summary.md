# EMA Hourly Continuation — CETUS/USDT P26_200

**Symbol:** CETUS/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.9530 |
| net_win_rate | 0.5382 |
| gross_profit_factor | 1.1775 |
| gross_win_rate | 0.5422 |
| sharpe_ratio | -0.1958 |
| sortino_ratio | -0.0444 |
| max_drawdown | 0.2294 |
| cagr | -0.0243 |
| net_avg_win | 91.2964 |
| net_avg_loss | -111.6210 |
| avg_hold_time_bars | 62.2169 |
| exposure | 0.7011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
