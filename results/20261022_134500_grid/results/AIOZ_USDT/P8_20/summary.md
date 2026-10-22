# EMA Hourly Continuation — AIOZ/USDT P8_20

**Symbol:** AIOZ/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1758 |
| net_profit_factor | 0.4728 |
| net_win_rate | 0.4283 |
| gross_profit_factor | 0.8526 |
| gross_win_rate | 0.4425 |
| sharpe_ratio | -11.7511 |
| sortino_ratio | -6.9172 |
| max_drawdown | 0.9998 |
| cagr | -0.9690 |
| net_avg_win | 11.9093 |
| net_avg_loss | -18.8717 |
| avg_hold_time_bars | 2.7247 |
| exposure | 0.2177 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
