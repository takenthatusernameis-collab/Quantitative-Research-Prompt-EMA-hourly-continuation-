# EMA Hourly Continuation — CGPT/USDT P50_200

**Symbol:** CGPT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.6782 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 0.9603 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -2.5303 |
| sortino_ratio | -0.6936 |
| max_drawdown | 0.5699 |
| cagr | -0.2827 |
| net_avg_win | 65.1604 |
| net_avg_loss | -88.3545 |
| avg_hold_time_bars | 22.2618 |
| exposure | 0.3865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
