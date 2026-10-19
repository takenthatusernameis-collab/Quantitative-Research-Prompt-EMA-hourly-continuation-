# EMA Hourly Continuation — KMNO/USDT P89_100

**Symbol:** KMNO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.2998 |
| net_win_rate | 0.3904 |
| gross_profit_factor | 0.6875 |
| gross_win_rate | 0.4144 |
| sharpe_ratio | -8.2983 |
| sortino_ratio | -2.7785 |
| max_drawdown | 0.9731 |
| cagr | -0.7683 |
| net_avg_win | 19.6535 |
| net_avg_loss | -41.9863 |
| avg_hold_time_bars | 3.1363 |
| exposure | 0.0786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
