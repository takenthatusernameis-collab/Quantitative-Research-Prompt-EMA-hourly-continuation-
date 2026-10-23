# EMA Hourly Continuation — HNT/USDT P21_200

**Symbol:** HNT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.7345 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9615 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -1.7673 |
| sortino_ratio | -0.4718 |
| max_drawdown | 0.4464 |
| cagr | -0.1981 |
| net_avg_win | 67.2751 |
| net_avg_loss | -89.0543 |
| avg_hold_time_bars | 40.6592 |
| exposure | 0.6561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
