# EMA Hourly Continuation — SYN/USDT P21_26

**Symbol:** SYN/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1155 |
| net_profit_factor | 0.2746 |
| net_win_rate | 0.3758 |
| gross_profit_factor | 0.6877 |
| gross_win_rate | 0.4139 |
| sharpe_ratio | -12.4140 |
| sortino_ratio | -6.0102 |
| max_drawdown | 0.9996 |
| cagr | -0.9572 |
| net_avg_win | 8.7213 |
| net_avg_loss | -19.1142 |
| avg_hold_time_bars | 2.2242 |
| exposure | 0.1168 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
