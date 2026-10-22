# EMA Hourly Continuation — DODO/USDT P89_100

**Symbol:** DODO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 174 |
| net_profit_factor | 0.6205 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.9225 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -1.9952 |
| sortino_ratio | -0.3764 |
| max_drawdown | 0.3704 |
| cagr | -0.1582 |
| net_avg_win | 69.4269 |
| net_avg_loss | -102.0528 |
| avg_hold_time_bars | 4.6034 |
| exposure | 0.0362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
