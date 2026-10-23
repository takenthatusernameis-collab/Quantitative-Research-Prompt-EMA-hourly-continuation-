# EMA Hourly Continuation — BABYDOGE/USDT P50_144

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 39 |
| net_profit_factor | 0.8759 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9398 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -0.2396 |
| sortino_ratio | -0.0213 |
| max_drawdown | 0.0529 |
| cagr | -0.0102 |
| net_avg_win | 94.5248 |
| net_avg_loss | -102.5260 |
| avg_hold_time_bars | 32.2308 |
| exposure | 0.0569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
