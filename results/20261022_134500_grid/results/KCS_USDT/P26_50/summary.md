# EMA Hourly Continuation — KCS/USDT P26_50

**Symbol:** KCS/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 993 |
| net_profit_factor | 0.1617 |
| net_win_rate | 0.2951 |
| gross_profit_factor | 0.6535 |
| gross_win_rate | 0.3797 |
| sharpe_ratio | -15.7125 |
| sortino_ratio | -7.4634 |
| max_drawdown | 1.0000 |
| cagr | -0.9818 |
| net_avg_win | 6.5836 |
| net_avg_loss | -17.0408 |
| avg_hold_time_bars | 3.6757 |
| exposure | 0.1659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
