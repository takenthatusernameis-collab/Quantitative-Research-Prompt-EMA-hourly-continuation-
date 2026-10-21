# EMA Hourly Continuation — XPR/USDT P12_100

**Symbol:** XPR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.7253 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.8962 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -2.2262 |
| sortino_ratio | -0.6955 |
| max_drawdown | 0.5793 |
| cagr | -0.2739 |
| net_avg_win | 63.6969 |
| net_avg_loss | -79.4890 |
| avg_hold_time_bars | 19.6203 |
| exposure | 0.4299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
