# EMA Hourly Continuation — G/USDT P12_50

**Symbol:** G/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 606 |
| net_profit_factor | 0.6524 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.8871 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -3.5143 |
| sortino_ratio | -1.3284 |
| max_drawdown | 0.7697 |
| cagr | -0.4563 |
| net_avg_win | 48.1401 |
| net_avg_loss | -65.9502 |
| avg_hold_time_bars | 11.9488 |
| exposure | 0.3807 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
