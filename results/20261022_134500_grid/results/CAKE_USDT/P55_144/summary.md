# EMA Hourly Continuation — CAKE/USDT P55_144

**Symbol:** CAKE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.4761 |
| net_win_rate | 0.4520 |
| gross_profit_factor | 0.8626 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -4.6896 |
| sortino_ratio | -1.4058 |
| max_drawdown | 0.8416 |
| cagr | -0.5050 |
| net_avg_win | 36.3868 |
| net_avg_loss | -63.0348 |
| avg_hold_time_bars | 11.7664 |
| exposure | 0.2450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
