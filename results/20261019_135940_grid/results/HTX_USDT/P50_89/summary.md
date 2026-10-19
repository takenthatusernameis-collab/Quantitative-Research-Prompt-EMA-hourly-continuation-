# EMA Hourly Continuation — HTX/USDT P50_89

**Symbol:** HTX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 787 |
| net_profit_factor | 0.2124 |
| net_win_rate | 0.2656 |
| gross_profit_factor | 0.6476 |
| gross_win_rate | 0.3494 |
| sharpe_ratio | -14.3942 |
| sortino_ratio | -6.1404 |
| max_drawdown | 0.9997 |
| cagr | -0.9620 |
| net_avg_win | 12.9000 |
| net_avg_loss | -21.9610 |
| avg_hold_time_bars | 5.2757 |
| exposure | 0.1879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
