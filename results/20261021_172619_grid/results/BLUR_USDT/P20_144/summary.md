# EMA Hourly Continuation — BLUR/USDT P20_144

**Symbol:** BLUR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.9302 |
| net_win_rate | 0.5317 |
| gross_profit_factor | 1.1350 |
| gross_win_rate | 0.5344 |
| sharpe_ratio | -0.3869 |
| sortino_ratio | -0.1060 |
| max_drawdown | 0.2222 |
| cagr | -0.0525 |
| net_avg_win | 87.8248 |
| net_avg_loss | -107.1836 |
| avg_hold_time_bars | 37.2755 |
| exposure | 0.6123 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
