# EMA Hourly Continuation — POL/USDT P26_144

**Symbol:** POL/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.6364 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 0.9904 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -2.5365 |
| sortino_ratio | -0.7635 |
| max_drawdown | 0.6233 |
| cagr | -0.3054 |
| net_avg_win | 46.2259 |
| net_avg_loss | -72.9561 |
| avg_hold_time_bars | 26.4018 |
| exposure | 0.5436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
