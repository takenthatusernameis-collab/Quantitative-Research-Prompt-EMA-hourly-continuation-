# EMA Hourly Continuation — WOO/USDT P8_20

**Symbol:** WOO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.7796 |
| net_win_rate | 0.5084 |
| gross_profit_factor | 1.0764 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -2.5284 |
| sortino_ratio | -0.9714 |
| max_drawdown | 0.6929 |
| cagr | -0.3591 |
| net_avg_win | 65.5625 |
| net_avg_loss | -86.9720 |
| avg_hold_time_bars | 5.3473 |
| exposure | 0.1735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
