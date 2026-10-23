# EMA Hourly Continuation — IOST/USDT P144_200

**Symbol:** IOST/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.4074 |
| net_win_rate | 0.4264 |
| gross_profit_factor | 0.8708 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -5.2642 |
| sortino_ratio | -1.4880 |
| max_drawdown | 0.8493 |
| cagr | -0.5199 |
| net_avg_win | 34.4371 |
| net_avg_loss | -62.8395 |
| avg_hold_time_bars | 4.9289 |
| exposure | 0.0883 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
