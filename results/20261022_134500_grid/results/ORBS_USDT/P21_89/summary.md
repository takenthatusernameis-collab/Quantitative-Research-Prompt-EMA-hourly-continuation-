# EMA Hourly Continuation — ORBS/USDT P21_89

**Symbol:** ORBS/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 771 |
| net_profit_factor | 0.5597 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.9636 |
| gross_win_rate | 0.4462 |
| sharpe_ratio | -6.7549 |
| sortino_ratio | -2.6360 |
| max_drawdown | 0.9643 |
| cagr | -0.7277 |
| net_avg_win | 36.8281 |
| net_avg_loss | -49.7622 |
| avg_hold_time_bars | 11.8495 |
| exposure | 0.4153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
