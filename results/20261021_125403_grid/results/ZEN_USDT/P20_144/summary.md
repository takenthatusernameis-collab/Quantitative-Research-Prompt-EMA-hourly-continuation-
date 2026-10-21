# EMA Hourly Continuation — ZEN/USDT P20_144

**Symbol:** ZEN/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.9238 |
| net_win_rate | 0.5283 |
| gross_profit_factor | 1.1155 |
| gross_win_rate | 0.5283 |
| sharpe_ratio | -0.4516 |
| sortino_ratio | -0.1253 |
| max_drawdown | 0.2784 |
| cagr | -0.0607 |
| net_avg_win | 90.0675 |
| net_avg_loss | -109.1957 |
| avg_hold_time_bars | 31.6819 |
| exposure | 0.5343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
