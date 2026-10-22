# EMA Hourly Continuation — 1INCH/USDT P12_100

**Symbol:** 1INCH/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.5378 |
| net_win_rate | 0.4391 |
| gross_profit_factor | 0.8331 |
| gross_win_rate | 0.4477 |
| sharpe_ratio | -5.1248 |
| sortino_ratio | -1.7395 |
| max_drawdown | 0.8845 |
| cagr | -0.5717 |
| net_avg_win | 40.0420 |
| net_avg_loss | -58.2919 |
| avg_hold_time_bars | 24.3482 |
| exposure | 0.6452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
