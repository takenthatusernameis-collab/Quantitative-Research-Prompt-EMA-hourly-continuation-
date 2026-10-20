# EMA Hourly Continuation — CGPT/USDT P89_144

**Symbol:** CGPT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.5619 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9560 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -3.7969 |
| sortino_ratio | -1.1491 |
| max_drawdown | 0.7589 |
| cagr | -0.4278 |
| net_avg_win | 43.5592 |
| net_avg_loss | -71.7048 |
| avg_hold_time_bars | 4.6082 |
| exposure | 0.0968 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
