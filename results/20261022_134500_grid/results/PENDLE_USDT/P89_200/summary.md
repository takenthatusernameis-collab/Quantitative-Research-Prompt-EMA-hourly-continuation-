# EMA Hourly Continuation — PENDLE/USDT P89_200

**Symbol:** PENDLE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.5264 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.7916 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -3.5645 |
| sortino_ratio | -1.0266 |
| max_drawdown | 0.7163 |
| cagr | -0.3888 |
| net_avg_win | 41.2971 |
| net_avg_loss | -64.3063 |
| avg_hold_time_bars | 10.4292 |
| exposure | 0.2010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
