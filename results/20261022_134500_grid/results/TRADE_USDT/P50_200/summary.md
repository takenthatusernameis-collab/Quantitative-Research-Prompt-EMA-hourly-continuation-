# EMA Hourly Continuation — TRADE/USDT P50_200

**Symbol:** TRADE/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.5765 |
| net_win_rate | 0.4201 |
| gross_profit_factor | 0.7583 |
| gross_win_rate | 0.4201 |
| sharpe_ratio | -3.4408 |
| sortino_ratio | -0.8815 |
| max_drawdown | 0.6764 |
| cagr | -0.3464 |
| net_avg_win | 62.9088 |
| net_avg_loss | -79.0596 |
| avg_hold_time_bars | 20.9645 |
| exposure | 0.3221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
