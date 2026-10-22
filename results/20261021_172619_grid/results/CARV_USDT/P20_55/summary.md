# EMA Hourly Continuation — CARV/USDT P20_55

**Symbol:** CARV/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.7233 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 0.9936 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -2.5265 |
| sortino_ratio | -0.8692 |
| max_drawdown | 0.5739 |
| cagr | -0.3284 |
| net_avg_win | 62.9639 |
| net_avg_loss | -84.8370 |
| avg_hold_time_bars | 9.7167 |
| exposure | 0.2548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
