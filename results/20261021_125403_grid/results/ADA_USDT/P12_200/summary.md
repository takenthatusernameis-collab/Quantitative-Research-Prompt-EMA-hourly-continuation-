# EMA Hourly Continuation — ADA/USDT P12_200

**Symbol:** ADA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.8060 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9787 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -1.1545 |
| sortino_ratio | -0.2788 |
| max_drawdown | 0.3203 |
| cagr | -0.1215 |
| net_avg_win | 81.8004 |
| net_avg_loss | -98.6891 |
| avg_hold_time_bars | 54.7133 |
| exposure | 0.7113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
