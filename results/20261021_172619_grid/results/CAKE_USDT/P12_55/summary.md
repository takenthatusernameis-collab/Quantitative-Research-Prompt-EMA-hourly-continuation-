# EMA Hourly Continuation — CAKE/USDT P12_55

**Symbol:** CAKE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.7421 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9956 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -2.4493 |
| sortino_ratio | -0.8451 |
| max_drawdown | 0.6438 |
| cagr | -0.3221 |
| net_avg_win | 62.4760 |
| net_avg_loss | -82.1871 |
| avg_hold_time_bars | 14.5129 |
| exposure | 0.3833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
