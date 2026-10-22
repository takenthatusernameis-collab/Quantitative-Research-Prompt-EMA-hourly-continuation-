# EMA Hourly Continuation — CETUS/USDT P20_89

**Symbol:** CETUS/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.8231 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 1.0088 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -1.6289 |
| sortino_ratio | -0.5452 |
| max_drawdown | 0.5280 |
| cagr | -0.2240 |
| net_avg_win | 80.2412 |
| net_avg_loss | -96.7843 |
| avg_hold_time_bars | 14.4691 |
| exposure | 0.3601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
