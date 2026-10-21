# EMA Hourly Continuation — GALA/USDT P100_200

**Symbol:** GALA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.7508 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.9211 |
| gross_win_rate | 0.4772 |
| sharpe_ratio | -1.4621 |
| sortino_ratio | -0.3237 |
| max_drawdown | 0.3874 |
| cagr | -0.1387 |
| net_avg_win | 81.9415 |
| net_avg_loss | -99.6106 |
| avg_hold_time_bars | 15.2656 |
| exposure | 0.1672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
