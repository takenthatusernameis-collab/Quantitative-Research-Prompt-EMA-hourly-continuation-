# EMA Hourly Continuation — COMP/USDT P144_200

**Symbol:** COMP/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 215 |
| net_profit_factor | 0.6449 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9537 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -1.8309 |
| sortino_ratio | -0.3861 |
| max_drawdown | 0.3746 |
| cagr | -0.1620 |
| net_avg_win | 61.3903 |
| net_avg_loss | -92.5774 |
| avg_hold_time_bars | 6.2930 |
| exposure | 0.0615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
