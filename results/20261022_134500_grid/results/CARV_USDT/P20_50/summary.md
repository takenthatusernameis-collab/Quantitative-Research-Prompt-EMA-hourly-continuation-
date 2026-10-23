# EMA Hourly Continuation — CARV/USDT P20_50

**Symbol:** CARV/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.5506 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.9746 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -5.7825 |
| sortino_ratio | -2.3688 |
| max_drawdown | 0.9095 |
| cagr | -0.6910 |
| net_avg_win | 34.0044 |
| net_avg_loss | -54.4365 |
| avg_hold_time_bars | 6.7020 |
| exposure | 0.2633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
