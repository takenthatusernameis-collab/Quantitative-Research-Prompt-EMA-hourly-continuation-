# EMA Hourly Continuation — LSK/USDT P50_200

**Symbol:** LSK/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.7300 |
| net_win_rate | 0.5101 |
| gross_profit_factor | 1.0446 |
| gross_win_rate | 0.5130 |
| sharpe_ratio | -1.7754 |
| sortino_ratio | -0.4647 |
| max_drawdown | 0.5234 |
| cagr | -0.2005 |
| net_avg_win | 66.0307 |
| net_avg_loss | -94.2035 |
| avg_hold_time_bars | 26.7913 |
| exposure | 0.4201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
