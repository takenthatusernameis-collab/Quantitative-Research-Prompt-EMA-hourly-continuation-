# EMA Hourly Continuation — BOME/USDT P26_89

**Symbol:** BOME/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.8498 |
| net_win_rate | 0.5148 |
| gross_profit_factor | 1.0318 |
| gross_win_rate | 0.5148 |
| sharpe_ratio | -0.9458 |
| sortino_ratio | -0.2958 |
| max_drawdown | 0.3551 |
| cagr | -0.1300 |
| net_avg_win | 68.4564 |
| net_avg_loss | -85.4555 |
| avg_hold_time_bars | 13.3650 |
| exposure | 0.2880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
