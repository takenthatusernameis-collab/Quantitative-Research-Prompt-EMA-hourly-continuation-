# EMA Hourly Continuation — UQC/USDT P21_26

**Symbol:** UQC/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.0340 |
| net_win_rate | 0.1984 |
| gross_profit_factor | 0.1542 |
| gross_win_rate | 0.2393 |
| sharpe_ratio | -12.9487 |
| sortino_ratio | -4.5226 |
| max_drawdown | 0.9985 |
| cagr | -0.9240 |
| net_avg_win | 3.4472 |
| net_avg_loss | -25.0888 |
| avg_hold_time_bars | 19.7724 |
| exposure | 0.4600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
