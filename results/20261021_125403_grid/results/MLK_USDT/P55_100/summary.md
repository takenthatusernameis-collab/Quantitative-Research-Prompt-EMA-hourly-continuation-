# EMA Hourly Continuation — MLK/USDT P55_100

**Symbol:** MLK/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.3294 |
| net_win_rate | 0.3117 |
| gross_profit_factor | 0.4869 |
| gross_win_rate | 0.3148 |
| sharpe_ratio | -6.1307 |
| sortino_ratio | -1.5631 |
| max_drawdown | 0.8459 |
| cagr | -0.5218 |
| net_avg_win | 41.0710 |
| net_avg_loss | -56.4707 |
| avg_hold_time_bars | 8.0988 |
| exposure | 0.1187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
