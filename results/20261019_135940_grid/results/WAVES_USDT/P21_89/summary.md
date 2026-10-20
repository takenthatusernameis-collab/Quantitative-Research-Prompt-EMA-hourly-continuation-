# EMA Hourly Continuation — WAVES/USDT P21_89

**Symbol:** WAVES/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 862 |
| net_profit_factor | 0.5282 |
| net_win_rate | 0.4350 |
| gross_profit_factor | 0.9150 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -7.1588 |
| sortino_ratio | -2.9312 |
| max_drawdown | 0.9778 |
| cagr | -0.7737 |
| net_avg_win | 29.1338 |
| net_avg_loss | -42.4757 |
| avg_hold_time_bars | 9.7587 |
| exposure | 0.3824 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
