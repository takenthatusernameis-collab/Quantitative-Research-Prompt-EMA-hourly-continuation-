# EMA Hourly Continuation — ENS/USDT P20_50

**Symbol:** ENS/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.7562 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 1.0068 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -2.2135 |
| sortino_ratio | -0.7142 |
| max_drawdown | 0.6006 |
| cagr | -0.2798 |
| net_avg_win | 69.0977 |
| net_avg_loss | -90.3045 |
| avg_hold_time_bars | 8.3550 |
| exposure | 0.1925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
