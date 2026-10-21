# EMA Hourly Continuation — RENDER/USDT P34_100

**Symbol:** RENDER/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.8122 |
| net_win_rate | 0.5027 |
| gross_profit_factor | 1.0025 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -1.3467 |
| sortino_ratio | -0.3986 |
| max_drawdown | 0.3929 |
| cagr | -0.1693 |
| net_avg_win | 77.2256 |
| net_avg_loss | -96.1241 |
| avg_hold_time_bars | 12.8533 |
| exposure | 0.2496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
