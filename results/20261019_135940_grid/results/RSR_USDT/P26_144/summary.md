# EMA Hourly Continuation — RSR/USDT P26_144

**Symbol:** RSR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.7459 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 0.9960 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -2.0312 |
| sortino_ratio | -0.6287 |
| max_drawdown | 0.5363 |
| cagr | -0.2588 |
| net_avg_win | 64.6416 |
| net_avg_loss | -85.9484 |
| avg_hold_time_bars | 20.2033 |
| exposure | 0.4426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
