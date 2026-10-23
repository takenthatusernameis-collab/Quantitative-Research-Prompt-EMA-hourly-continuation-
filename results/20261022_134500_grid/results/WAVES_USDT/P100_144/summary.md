# EMA Hourly Continuation — WAVES/USDT P100_144

**Symbol:** WAVES/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 582 |
| net_profit_factor | 0.3999 |
| net_win_rate | 0.4072 |
| gross_profit_factor | 0.8527 |
| gross_win_rate | 0.4399 |
| sharpe_ratio | -7.4852 |
| sortino_ratio | -2.5663 |
| max_drawdown | 0.9650 |
| cagr | -0.7321 |
| net_avg_win | 27.0847 |
| net_avg_loss | -46.5311 |
| avg_hold_time_bars | 3.9588 |
| exposure | 0.1047 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
