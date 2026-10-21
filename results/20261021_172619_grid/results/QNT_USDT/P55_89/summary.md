# EMA Hourly Continuation — QNT/USDT P55_89

**Symbol:** QNT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.5643 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.8246 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -3.0756 |
| sortino_ratio | -0.7994 |
| max_drawdown | 0.6337 |
| cagr | -0.3056 |
| net_avg_win | 51.4481 |
| net_avg_loss | -76.9141 |
| avg_hold_time_bars | 6.2667 |
| exposure | 0.0940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
