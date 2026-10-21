# EMA Hourly Continuation — API3/USDT P20_50

**Symbol:** API3/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.7363 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9809 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -2.5741 |
| sortino_ratio | -0.8744 |
| max_drawdown | 0.6419 |
| cagr | -0.3309 |
| net_avg_win | 64.2918 |
| net_avg_loss | -83.6792 |
| avg_hold_time_bars | 7.5035 |
| exposure | 0.1924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
