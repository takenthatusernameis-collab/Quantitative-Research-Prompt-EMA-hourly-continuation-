# EMA Hourly Continuation — MNT/USDT P8_100

**Symbol:** MNT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.5207 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.8760 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -3.9371 |
| sortino_ratio | -1.3353 |
| max_drawdown | 0.8136 |
| cagr | -0.4834 |
| net_avg_win | 31.2958 |
| net_avg_loss | -53.9635 |
| avg_hold_time_bars | 26.0051 |
| exposure | 0.7021 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
