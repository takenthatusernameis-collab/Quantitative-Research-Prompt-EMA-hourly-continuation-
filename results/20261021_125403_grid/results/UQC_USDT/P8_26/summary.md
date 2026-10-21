# EMA Hourly Continuation — UQC/USDT P8_26

**Symbol:** UQC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.3917 |
| net_win_rate | 0.3293 |
| gross_profit_factor | 0.6373 |
| gross_win_rate | 0.3535 |
| sharpe_ratio | -5.7791 |
| sortino_ratio | -1.4734 |
| max_drawdown | 0.8353 |
| cagr | -0.5080 |
| net_avg_win | 49.2066 |
| net_avg_loss | -61.6779 |
| avg_hold_time_bars | 38.4230 |
| exposure | 0.5756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
