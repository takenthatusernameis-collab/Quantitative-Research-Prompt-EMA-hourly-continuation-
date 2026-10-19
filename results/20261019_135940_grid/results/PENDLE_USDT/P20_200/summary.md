# EMA Hourly Continuation — PENDLE/USDT P20_200

**Symbol:** PENDLE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.6184 |
| net_win_rate | 0.4486 |
| gross_profit_factor | 0.8459 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -2.8559 |
| sortino_ratio | -0.7156 |
| max_drawdown | 0.5985 |
| cagr | -0.2900 |
| net_avg_win | 64.9043 |
| net_avg_loss | -85.3935 |
| avg_hold_time_bars | 49.1745 |
| exposure | 0.7175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
