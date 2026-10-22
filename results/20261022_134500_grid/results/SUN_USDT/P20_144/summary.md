# EMA Hourly Continuation — SUN/USDT P20_144

**Symbol:** SUN/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.4263 |
| net_win_rate | 0.3978 |
| gross_profit_factor | 0.8342 |
| gross_win_rate | 0.4418 |
| sharpe_ratio | -6.2361 |
| sortino_ratio | -1.8695 |
| max_drawdown | 0.9084 |
| cagr | -0.6108 |
| net_avg_win | 37.2634 |
| net_avg_loss | -57.7359 |
| avg_hold_time_bars | 27.5077 |
| exposure | 0.5664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
