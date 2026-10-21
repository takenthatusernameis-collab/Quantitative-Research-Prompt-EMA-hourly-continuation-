# EMA Hourly Continuation — T/USDT P26_50

**Symbol:** T/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.6253 |
| net_win_rate | 0.4809 |
| gross_profit_factor | 0.9877 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -3.7896 |
| sortino_ratio | -1.2407 |
| max_drawdown | 0.7686 |
| cagr | -0.4346 |
| net_avg_win | 50.5021 |
| net_avg_loss | -74.8299 |
| avg_hold_time_bars | 6.9427 |
| exposure | 0.1646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
