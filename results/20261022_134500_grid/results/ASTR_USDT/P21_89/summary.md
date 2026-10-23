# EMA Hourly Continuation — ASTR/USDT P21_89

**Symbol:** ASTR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 640 |
| net_profit_factor | 0.6602 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 1.0638 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -3.5155 |
| sortino_ratio | -1.2470 |
| max_drawdown | 0.7997 |
| cagr | -0.4526 |
| net_avg_win | 47.5967 |
| net_avg_loss | -71.6403 |
| avg_hold_time_bars | 13.8109 |
| exposure | 0.4000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
