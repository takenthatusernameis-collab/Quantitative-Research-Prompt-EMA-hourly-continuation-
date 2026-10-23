# EMA Hourly Continuation — BICO/USDT P50_100

**Symbol:** BICO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.5476 |
| net_win_rate | 0.4530 |
| gross_profit_factor | 0.8507 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -4.3523 |
| sortino_ratio | -1.5093 |
| max_drawdown | 0.8330 |
| cagr | -0.5046 |
| net_avg_win | 37.1507 |
| net_avg_loss | -56.1863 |
| avg_hold_time_bars | 8.2567 |
| exposure | 0.2237 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
