# EMA Hourly Continuation — CAKE/USDT P89_100

**Symbol:** CAKE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.2047 |
| net_win_rate | 0.3444 |
| gross_profit_factor | 0.7934 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -9.9622 |
| sortino_ratio | -3.3724 |
| max_drawdown | 0.9896 |
| cagr | -0.8367 |
| net_avg_win | 14.4661 |
| net_avg_loss | -37.1356 |
| avg_hold_time_bars | 2.0861 |
| exposure | 0.0485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
