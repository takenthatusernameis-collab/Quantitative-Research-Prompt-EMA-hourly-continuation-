# EMA Hourly Continuation — BICO/USDT P12_100

**Symbol:** BICO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.8703 |
| net_win_rate | 0.5109 |
| gross_profit_factor | 1.0378 |
| gross_win_rate | 0.5109 |
| sharpe_ratio | -0.9414 |
| sortino_ratio | -0.3035 |
| max_drawdown | 0.3612 |
| cagr | -0.1345 |
| net_avg_win | 79.0919 |
| net_avg_loss | -94.9294 |
| avg_hold_time_bars | 25.5426 |
| exposure | 0.5863 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
