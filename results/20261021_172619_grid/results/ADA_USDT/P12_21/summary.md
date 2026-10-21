# EMA Hourly Continuation — ADA/USDT P12_21

**Symbol:** ADA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.9068 |
| net_win_rate | 0.5698 |
| gross_profit_factor | 1.3148 |
| gross_win_rate | 0.5698 |
| sharpe_ratio | -0.4535 |
| sortino_ratio | -0.1063 |
| max_drawdown | 0.1802 |
| cagr | -0.0498 |
| net_avg_win | 79.6760 |
| net_avg_loss | -116.3672 |
| avg_hold_time_bars | 4.3295 |
| exposure | 0.0508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
