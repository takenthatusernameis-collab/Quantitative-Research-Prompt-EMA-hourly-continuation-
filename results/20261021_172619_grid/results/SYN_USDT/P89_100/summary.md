# EMA Hourly Continuation — SYN/USDT P89_100

**Symbol:** SYN/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 164 |
| net_profit_factor | 0.7864 |
| net_win_rate | 0.5244 |
| gross_profit_factor | 1.0995 |
| gross_win_rate | 0.5244 |
| sharpe_ratio | -0.9478 |
| sortino_ratio | -0.1749 |
| max_drawdown | 0.2121 |
| cagr | -0.0775 |
| net_avg_win | 78.4784 |
| net_avg_loss | -110.0353 |
| avg_hold_time_bars | 5.8415 |
| exposure | 0.0435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
