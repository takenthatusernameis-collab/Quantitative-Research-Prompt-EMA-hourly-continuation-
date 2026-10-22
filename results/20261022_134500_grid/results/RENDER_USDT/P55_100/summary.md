# EMA Hourly Continuation — RENDER/USDT P55_100

**Symbol:** RENDER/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.5994 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9550 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -4.4275 |
| sortino_ratio | -1.5743 |
| max_drawdown | 0.8171 |
| cagr | -0.5289 |
| net_avg_win | 46.0637 |
| net_avg_loss | -70.1377 |
| avg_hold_time_bars | 5.2102 |
| exposure | 0.1504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
