# EMA Hourly Continuation — DUSK/USDT P8_26

**Symbol:** DUSK/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1500 |
| net_profit_factor | 0.6131 |
| net_win_rate | 0.4633 |
| gross_profit_factor | 1.1002 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -7.7454 |
| sortino_ratio | -4.2150 |
| max_drawdown | 0.9943 |
| cagr | -0.8714 |
| net_avg_win | 22.6651 |
| net_avg_loss | -31.9184 |
| avg_hold_time_bars | 4.2287 |
| exposure | 0.2883 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
