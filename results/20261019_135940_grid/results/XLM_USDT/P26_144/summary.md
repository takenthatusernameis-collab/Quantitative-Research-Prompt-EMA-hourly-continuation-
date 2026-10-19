# EMA Hourly Continuation — XLM/USDT P26_144

**Symbol:** XLM/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.4484 |
| net_win_rate | 0.4577 |
| gross_profit_factor | 0.8257 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -4.5608 |
| sortino_ratio | -1.3903 |
| max_drawdown | 0.8362 |
| cagr | -0.5048 |
| net_avg_win | 30.3517 |
| net_avg_loss | -57.1338 |
| avg_hold_time_bars | 22.2062 |
| exposure | 0.4895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
