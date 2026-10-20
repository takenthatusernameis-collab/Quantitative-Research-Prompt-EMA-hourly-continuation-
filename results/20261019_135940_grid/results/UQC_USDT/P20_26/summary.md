# EMA Hourly Continuation — UQC/USDT P20_26

**Symbol:** UQC/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.0453 |
| net_win_rate | 0.2053 |
| gross_profit_factor | 0.1928 |
| gross_win_rate | 0.2471 |
| sharpe_ratio | -12.8660 |
| sortino_ratio | -4.5093 |
| max_drawdown | 0.9984 |
| cagr | -0.9225 |
| net_avg_win | 4.3831 |
| net_avg_loss | -25.0181 |
| avg_hold_time_bars | 19.6027 |
| exposure | 0.4667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
