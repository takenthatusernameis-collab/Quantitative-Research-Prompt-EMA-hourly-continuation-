# EMA Hourly Continuation — BICO/USDT P26_100

**Symbol:** BICO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.5536 |
| net_win_rate | 0.4413 |
| gross_profit_factor | 0.7967 |
| gross_win_rate | 0.4476 |
| sharpe_ratio | -4.4303 |
| sortino_ratio | -1.5692 |
| max_drawdown | 0.8546 |
| cagr | -0.5228 |
| net_avg_win | 37.6451 |
| net_avg_loss | -53.7082 |
| avg_hold_time_bars | 13.3540 |
| exposure | 0.3824 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
