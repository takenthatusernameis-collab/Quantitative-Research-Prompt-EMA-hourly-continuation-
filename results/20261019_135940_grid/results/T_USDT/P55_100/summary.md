# EMA Hourly Continuation — T/USDT P55_100

**Symbol:** T/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.4193 |
| net_win_rate | 0.4236 |
| gross_profit_factor | 0.7842 |
| gross_win_rate | 0.4494 |
| sharpe_ratio | -6.0981 |
| sortino_ratio | -1.9957 |
| max_drawdown | 0.9193 |
| cagr | -0.6277 |
| net_avg_win | 28.7940 |
| net_avg_loss | -50.4640 |
| avg_hold_time_bars | 8.2744 |
| exposure | 0.2033 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
