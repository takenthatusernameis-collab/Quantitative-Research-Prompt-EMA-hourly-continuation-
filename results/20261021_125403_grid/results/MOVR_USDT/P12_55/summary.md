# EMA Hourly Continuation — MOVR/USDT P12_55

**Symbol:** MOVR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.7987 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.0127 |
| gross_win_rate | 0.5067 |
| sharpe_ratio | -1.7308 |
| sortino_ratio | -0.6451 |
| max_drawdown | 0.5757 |
| cagr | -0.2584 |
| net_avg_win | 61.2585 |
| net_avg_loss | -78.7676 |
| avg_hold_time_bars | 11.7081 |
| exposure | 0.3592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
