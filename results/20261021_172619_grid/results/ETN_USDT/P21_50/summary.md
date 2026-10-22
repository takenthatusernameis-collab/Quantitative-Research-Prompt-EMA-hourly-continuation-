# EMA Hourly Continuation — ETN/USDT P21_50

**Symbol:** ETN/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.5052 |
| net_win_rate | 0.3983 |
| gross_profit_factor | 0.6563 |
| gross_win_rate | 0.3983 |
| sharpe_ratio | -4.3543 |
| sortino_ratio | -1.2560 |
| max_drawdown | 0.7107 |
| cagr | -0.4407 |
| net_avg_win | 51.7912 |
| net_avg_loss | -67.8553 |
| avg_hold_time_bars | 9.3782 |
| exposure | 0.1778 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
