# EMA Hourly Continuation — ELON/USDT P8_144

**Symbol:** ELON/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.7453 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.8961 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -2.0510 |
| sortino_ratio | -0.5938 |
| max_drawdown | 0.5102 |
| cagr | -0.2393 |
| net_avg_win | 74.5680 |
| net_avg_loss | -88.2790 |
| avg_hold_time_bars | 37.2837 |
| exposure | 0.7050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
