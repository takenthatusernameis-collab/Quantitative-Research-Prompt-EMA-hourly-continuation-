# EMA Hourly Continuation — FLUX/USDT P20_144

**Symbol:** FLUX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.6927 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9826 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -2.6598 |
| sortino_ratio | -0.8447 |
| max_drawdown | 0.6632 |
| cagr | -0.3277 |
| net_avg_win | 58.7612 |
| net_avg_loss | -78.6593 |
| avg_hold_time_bars | 24.4254 |
| exposure | 0.5585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
