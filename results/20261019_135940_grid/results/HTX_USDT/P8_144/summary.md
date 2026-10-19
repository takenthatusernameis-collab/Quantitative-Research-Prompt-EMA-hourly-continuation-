# EMA Hourly Continuation — HTX/USDT P8_144

**Symbol:** HTX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.4204 |
| net_win_rate | 0.3628 |
| gross_profit_factor | 0.9013 |
| gross_win_rate | 0.4192 |
| sharpe_ratio | -8.5070 |
| sortino_ratio | -2.7860 |
| max_drawdown | 0.9790 |
| cagr | -0.7812 |
| net_avg_win | 36.7664 |
| net_avg_loss | -49.7924 |
| avg_hold_time_bars | 30.9117 |
| exposure | 0.7442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
