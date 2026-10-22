# EMA Hourly Continuation — QNT/USDT P55_200

**Symbol:** QNT/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.7155 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0813 |
| gross_win_rate | 0.5160 |
| sharpe_ratio | -2.2465 |
| sortino_ratio | -0.6668 |
| max_drawdown | 0.5882 |
| cagr | -0.2690 |
| net_avg_win | 61.1534 |
| net_avg_loss | -89.4673 |
| avg_hold_time_bars | 17.0160 |
| exposure | 0.3388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
