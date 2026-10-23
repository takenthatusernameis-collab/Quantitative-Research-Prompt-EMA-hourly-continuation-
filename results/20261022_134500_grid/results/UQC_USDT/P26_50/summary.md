# EMA Hourly Continuation — UQC/USDT P26_50

**Symbol:** UQC/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.1285 |
| net_win_rate | 0.2549 |
| gross_profit_factor | 0.3361 |
| gross_win_rate | 0.2696 |
| sharpe_ratio | -9.4661 |
| sortino_ratio | -2.7441 |
| max_drawdown | 0.9775 |
| cagr | -0.7779 |
| net_avg_win | 13.8534 |
| net_avg_loss | -36.8943 |
| avg_hold_time_bars | 27.2917 |
| exposure | 0.5040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
