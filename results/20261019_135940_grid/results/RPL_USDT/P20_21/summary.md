# EMA Hourly Continuation — RPL/USDT P20_21

**Symbol:** RPL/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1112 |
| net_profit_factor | 0.1611 |
| net_win_rate | 0.3345 |
| gross_profit_factor | 0.6933 |
| gross_win_rate | 0.4218 |
| sharpe_ratio | -14.7774 |
| sortino_ratio | -7.1553 |
| max_drawdown | 1.0000 |
| cagr | -0.9817 |
| net_avg_win | 5.1619 |
| net_avg_loss | -16.1078 |
| avg_hold_time_bars | 2.5971 |
| exposure | 0.1307 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
