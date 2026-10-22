# EMA Hourly Continuation — LUNC/USDT P89_200

**Symbol:** LUNC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.5581 |
| net_win_rate | 0.4652 |
| gross_profit_factor | 0.9340 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -4.0306 |
| sortino_ratio | -1.1959 |
| max_drawdown | 0.7817 |
| cagr | -0.4425 |
| net_avg_win | 46.9520 |
| net_avg_loss | -73.1664 |
| avg_hold_time_bars | 11.0831 |
| exposure | 0.2242 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
