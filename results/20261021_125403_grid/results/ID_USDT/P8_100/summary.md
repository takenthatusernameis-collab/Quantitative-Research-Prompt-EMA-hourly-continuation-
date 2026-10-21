# EMA Hourly Continuation — ID/USDT P8_100

**Symbol:** ID/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.8037 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 0.9915 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -1.5220 |
| sortino_ratio | -0.4764 |
| max_drawdown | 0.4389 |
| cagr | -0.1989 |
| net_avg_win | 73.0941 |
| net_avg_loss | -89.8266 |
| avg_hold_time_bars | 31.0890 |
| exposure | 0.6795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
