# EMA Hourly Continuation — CAKE/USDT P12_21

**Symbol:** CAKE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1418 |
| net_profit_factor | 0.2762 |
| net_win_rate | 0.3921 |
| gross_profit_factor | 0.9122 |
| gross_win_rate | 0.4520 |
| sharpe_ratio | -14.4356 |
| sortino_ratio | -7.8598 |
| max_drawdown | 1.0000 |
| cagr | -0.9840 |
| net_avg_win | 6.8620 |
| net_avg_loss | -16.0266 |
| avg_hold_time_bars | 2.3999 |
| exposure | 0.1547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
