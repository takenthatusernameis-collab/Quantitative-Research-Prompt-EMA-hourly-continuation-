# EMA Hourly Continuation — FLUX/USDT P8_20

**Symbol:** FLUX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.8428 |
| net_win_rate | 0.5266 |
| gross_profit_factor | 1.1297 |
| gross_win_rate | 0.5266 |
| sharpe_ratio | -1.3473 |
| sortino_ratio | -0.4380 |
| max_drawdown | 0.5332 |
| cagr | -0.1836 |
| net_avg_win | 80.1649 |
| net_avg_loss | -105.8143 |
| avg_hold_time_bars | 5.5207 |
| exposure | 0.1272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
