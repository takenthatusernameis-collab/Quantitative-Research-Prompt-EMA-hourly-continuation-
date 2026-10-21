# EMA Hourly Continuation — POLYX/USDT P89_144

**Symbol:** POLYX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.8049 |
| net_win_rate | 0.5369 |
| gross_profit_factor | 1.1467 |
| gross_win_rate | 0.5369 |
| sharpe_ratio | -1.2173 |
| sortino_ratio | -0.3239 |
| max_drawdown | 0.3252 |
| cagr | -0.1389 |
| net_avg_win | 70.9360 |
| net_avg_loss | -102.1691 |
| avg_hold_time_bars | 7.7257 |
| exposure | 0.1190 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
