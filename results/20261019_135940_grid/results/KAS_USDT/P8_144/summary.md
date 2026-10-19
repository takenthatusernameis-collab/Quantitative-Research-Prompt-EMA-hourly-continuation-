# EMA Hourly Continuation — KAS/USDT P8_144

**Symbol:** KAS/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.6318 |
| net_win_rate | 0.4779 |
| gross_profit_factor | 0.9673 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -3.6487 |
| sortino_ratio | -1.2345 |
| max_drawdown | 0.7897 |
| cagr | -0.4542 |
| net_avg_win | 47.7109 |
| net_avg_loss | -69.1246 |
| avg_hold_time_bars | 27.2415 |
| exposure | 0.7281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
