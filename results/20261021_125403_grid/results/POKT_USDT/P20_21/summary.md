# EMA Hourly Continuation — POKT/USDT P20_21

**Symbol:** POKT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.3861 |
| net_win_rate | 0.3180 |
| gross_profit_factor | 0.5551 |
| gross_win_rate | 0.3216 |
| sharpe_ratio | -5.5155 |
| sortino_ratio | -1.3131 |
| max_drawdown | 0.7923 |
| cagr | -0.4597 |
| net_avg_win | 55.0911 |
| net_avg_loss | -66.5407 |
| avg_hold_time_bars | 6.3569 |
| exposure | 0.0814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
