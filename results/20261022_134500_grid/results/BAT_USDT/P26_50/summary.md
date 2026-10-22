# EMA Hourly Continuation — BAT/USDT P26_50

**Symbol:** BAT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 956 |
| net_profit_factor | 0.4192 |
| net_win_rate | 0.4425 |
| gross_profit_factor | 0.8707 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -7.8219 |
| sortino_ratio | -3.4387 |
| max_drawdown | 0.9850 |
| cagr | -0.8113 |
| net_avg_win | 16.8023 |
| net_avg_loss | -31.8117 |
| avg_hold_time_bars | 4.0879 |
| exposure | 0.1776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
