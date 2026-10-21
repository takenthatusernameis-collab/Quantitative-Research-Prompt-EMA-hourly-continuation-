# EMA Hourly Continuation — PROM/USDT P8_20

**Symbol:** PROM/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.5273 |
| net_win_rate | 0.4394 |
| gross_profit_factor | 0.8045 |
| gross_win_rate | 0.4394 |
| sharpe_ratio | -5.1644 |
| sortino_ratio | -1.8667 |
| max_drawdown | 0.8886 |
| cagr | -0.5803 |
| net_avg_win | 34.9623 |
| net_avg_loss | -51.9788 |
| avg_hold_time_bars | 6.3432 |
| exposure | 0.1857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
