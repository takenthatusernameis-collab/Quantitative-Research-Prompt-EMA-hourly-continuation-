# EMA Hourly Continuation — BICO/USDT P55_144

**Symbol:** BICO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7111 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.8870 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -2.0758 |
| sortino_ratio | -0.5712 |
| max_drawdown | 0.4974 |
| cagr | -0.2316 |
| net_avg_win | 67.6647 |
| net_avg_loss | -84.5856 |
| avg_hold_time_bars | 17.4118 |
| exposure | 0.2960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
