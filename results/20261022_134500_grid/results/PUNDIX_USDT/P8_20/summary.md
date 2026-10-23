# EMA Hourly Continuation — PUNDIX/USDT P8_20

**Symbol:** PUNDIX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1519 |
| net_profit_factor | 0.2837 |
| net_win_rate | 0.4003 |
| gross_profit_factor | 0.6844 |
| gross_win_rate | 0.4345 |
| sharpe_ratio | -12.9143 |
| sortino_ratio | -7.1610 |
| max_drawdown | 0.9999 |
| cagr | -0.9733 |
| net_avg_win | 6.5150 |
| net_avg_loss | -15.3238 |
| avg_hold_time_bars | 3.8795 |
| exposure | 0.2679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
