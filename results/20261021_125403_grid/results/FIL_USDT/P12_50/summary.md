# EMA Hourly Continuation — FIL/USDT P12_50

**Symbol:** FIL/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.7769 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0120 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -1.8826 |
| sortino_ratio | -0.6511 |
| max_drawdown | 0.5378 |
| cagr | -0.2592 |
| net_avg_win | 62.8912 |
| net_avg_loss | -82.3592 |
| avg_hold_time_bars | 12.3133 |
| exposure | 0.3252 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
