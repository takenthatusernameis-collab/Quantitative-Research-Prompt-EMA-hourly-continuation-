# EMA Hourly Continuation — SUN/USDT P55_144

**Symbol:** SUN/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.4590 |
| net_win_rate | 0.4134 |
| gross_profit_factor | 0.7778 |
| gross_win_rate | 0.4195 |
| sharpe_ratio | -4.8097 |
| sortino_ratio | -1.2508 |
| max_drawdown | 0.7750 |
| cagr | -0.4443 |
| net_avg_win | 48.2060 |
| net_avg_loss | -74.0112 |
| avg_hold_time_bars | 17.3252 |
| exposure | 0.2579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
