# EMA Hourly Continuation — CAKE/USDT P12_20

**Symbol:** CAKE/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1426 |
| net_profit_factor | 0.2621 |
| net_win_rate | 0.3787 |
| gross_profit_factor | 0.9080 |
| gross_win_rate | 0.4411 |
| sharpe_ratio | -15.2083 |
| sortino_ratio | -8.3457 |
| max_drawdown | 1.0000 |
| cagr | -0.9882 |
| net_avg_win | 6.5778 |
| net_avg_loss | -15.2956 |
| avg_hold_time_bars | 2.2882 |
| exposure | 0.1483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
