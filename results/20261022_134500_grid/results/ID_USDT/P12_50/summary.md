# EMA Hourly Continuation — ID/USDT P12_50

**Symbol:** ID/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 937 |
| net_profit_factor | 0.5728 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.9800 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -5.3063 |
| sortino_ratio | -2.2801 |
| max_drawdown | 0.9390 |
| cagr | -0.6655 |
| net_avg_win | 28.3592 |
| net_avg_loss | -44.3960 |
| avg_hold_time_bars | 8.5923 |
| exposure | 0.3643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
