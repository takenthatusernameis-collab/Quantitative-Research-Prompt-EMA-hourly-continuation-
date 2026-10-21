# EMA Hourly Continuation — LPT/USDT P55_144

**Symbol:** LPT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.7173 |
| net_win_rate | 0.4827 |
| gross_profit_factor | 0.9125 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -1.8470 |
| sortino_ratio | -0.4900 |
| max_drawdown | 0.4374 |
| cagr | -0.2009 |
| net_avg_win | 65.4292 |
| net_avg_loss | -85.1026 |
| avg_hold_time_bars | 15.3208 |
| exposure | 0.2410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
