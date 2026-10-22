# EMA Hourly Continuation — BSV/USDT P55_144

**Symbol:** BSV/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.4466 |
| net_win_rate | 0.4033 |
| gross_profit_factor | 0.7595 |
| gross_win_rate | 0.4177 |
| sharpe_ratio | -6.2046 |
| sortino_ratio | -2.0518 |
| max_drawdown | 0.9187 |
| cagr | -0.6319 |
| net_avg_win | 33.2471 |
| net_avg_loss | -50.3074 |
| avg_hold_time_bars | 11.2315 |
| exposure | 0.2823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
