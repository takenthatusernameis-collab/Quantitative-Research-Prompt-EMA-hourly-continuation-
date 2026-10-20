# EMA Hourly Continuation — MASK/USDT P8_89

**Symbol:** MASK/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 758 |
| net_profit_factor | 0.4602 |
| net_win_rate | 0.4393 |
| gross_profit_factor | 0.7703 |
| gross_win_rate | 0.4551 |
| sharpe_ratio | -6.1292 |
| sortino_ratio | -2.3627 |
| max_drawdown | 0.9464 |
| cagr | -0.6833 |
| net_avg_win | 24.1754 |
| net_avg_loss | -41.1604 |
| avg_hold_time_bars | 18.5765 |
| exposure | 0.6400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
