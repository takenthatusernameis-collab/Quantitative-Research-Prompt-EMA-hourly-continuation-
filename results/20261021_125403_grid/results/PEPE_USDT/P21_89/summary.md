# EMA Hourly Continuation — PEPE/USDT P21_89

**Symbol:** PEPE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.7429 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.8998 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -1.9143 |
| sortino_ratio | -0.5579 |
| max_drawdown | 0.4949 |
| cagr | -0.2264 |
| net_avg_win | 69.0023 |
| net_avg_loss | -84.0153 |
| avg_hold_time_bars | 19.5656 |
| exposure | 0.3726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
