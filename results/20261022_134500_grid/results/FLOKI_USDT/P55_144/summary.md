# EMA Hourly Continuation — FLOKI/USDT P55_144

**Symbol:** FLOKI/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.6215 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.8767 |
| gross_win_rate | 0.4696 |
| sharpe_ratio | -3.3392 |
| sortino_ratio | -1.0480 |
| max_drawdown | 0.7171 |
| cagr | -0.3908 |
| net_avg_win | 50.6108 |
| net_avg_loss | -71.5210 |
| avg_hold_time_bars | 13.0951 |
| exposure | 0.2940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
