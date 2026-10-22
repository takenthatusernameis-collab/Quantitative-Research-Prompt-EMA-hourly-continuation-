# EMA Hourly Continuation — XLM/USDT P26_50

**Symbol:** XLM/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 987 |
| net_profit_factor | 0.2803 |
| net_win_rate | 0.4417 |
| gross_profit_factor | 0.8369 |
| gross_win_rate | 0.4721 |
| sharpe_ratio | -9.3153 |
| sortino_ratio | -4.1419 |
| max_drawdown | 0.9951 |
| cagr | -0.8784 |
| net_avg_win | 8.8879 |
| net_avg_loss | -25.0904 |
| avg_hold_time_bars | 3.5998 |
| exposure | 0.1615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
