# EMA Hourly Continuation — XPR/USDT P8_20

**Symbol:** XPR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.6362 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.8864 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -2.4788 |
| sortino_ratio | -0.6224 |
| max_drawdown | 0.5213 |
| cagr | -0.2481 |
| net_avg_win | 61.6621 |
| net_avg_loss | -86.2242 |
| avg_hold_time_bars | 9.7630 |
| exposure | 0.1367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
