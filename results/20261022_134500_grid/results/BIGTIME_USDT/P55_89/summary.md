# EMA Hourly Continuation — BIGTIME/USDT P55_89

**Symbol:** BIGTIME/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.5614 |
| net_win_rate | 0.4612 |
| gross_profit_factor | 0.9505 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -5.0150 |
| sortino_ratio | -1.8022 |
| max_drawdown | 0.8885 |
| cagr | -0.5748 |
| net_avg_win | 38.1141 |
| net_avg_loss | -58.1076 |
| avg_hold_time_bars | 4.6584 |
| exposure | 0.1358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
