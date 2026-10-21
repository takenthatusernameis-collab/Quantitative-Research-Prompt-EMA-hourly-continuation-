# EMA Hourly Continuation — CAKE/USDT P12_26

**Symbol:** CAKE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.7211 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0576 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -2.4659 |
| sortino_ratio | -0.7481 |
| max_drawdown | 0.5981 |
| cagr | -0.2911 |
| net_avg_win | 66.4948 |
| net_avg_loss | -94.3027 |
| avg_hold_time_bars | 6.0854 |
| exposure | 0.1231 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
