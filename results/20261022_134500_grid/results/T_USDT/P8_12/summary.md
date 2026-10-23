# EMA Hourly Continuation — T/USDT P8_12

**Symbol:** T/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1322 |
| net_profit_factor | 0.2733 |
| net_win_rate | 0.3986 |
| gross_profit_factor | 0.8731 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -13.0615 |
| sortino_ratio | -6.7917 |
| max_drawdown | 0.9999 |
| cagr | -0.9715 |
| net_avg_win | 7.1337 |
| net_avg_loss | -17.3059 |
| avg_hold_time_bars | 3.2625 |
| exposure | 0.1952 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
