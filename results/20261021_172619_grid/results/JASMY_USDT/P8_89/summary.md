# EMA Hourly Continuation — JASMY/USDT P8_89

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.9122 |
| net_win_rate | 0.5231 |
| gross_profit_factor | 1.0883 |
| gross_win_rate | 0.5231 |
| sharpe_ratio | -0.6062 |
| sortino_ratio | -0.1945 |
| max_drawdown | 0.3337 |
| cagr | -0.0910 |
| net_avg_win | 85.1826 |
| net_avg_loss | -102.4423 |
| avg_hold_time_bars | 27.6620 |
| exposure | 0.6249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
