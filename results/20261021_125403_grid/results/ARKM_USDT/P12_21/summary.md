# EMA Hourly Continuation — ARKM/USDT P12_21

**Symbol:** ARKM/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.5934 |
| net_win_rate | 0.4423 |
| gross_profit_factor | 0.7890 |
| gross_win_rate | 0.4423 |
| sharpe_ratio | -2.9045 |
| sortino_ratio | -0.7298 |
| max_drawdown | 0.5674 |
| cagr | -0.2837 |
| net_avg_win | 59.9975 |
| net_avg_loss | -80.1916 |
| avg_hold_time_bars | 4.6026 |
| exposure | 0.0653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
