# EMA Hourly Continuation — LPT/USDT P20_100

**Symbol:** LPT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.6571 |
| net_win_rate | 0.4468 |
| gross_profit_factor | 0.8223 |
| gross_win_rate | 0.4468 |
| sharpe_ratio | -3.2732 |
| sortino_ratio | -1.0637 |
| max_drawdown | 0.7183 |
| cagr | -0.3887 |
| net_avg_win | 57.8533 |
| net_avg_loss | -71.0990 |
| avg_hold_time_bars | 16.3745 |
| exposure | 0.3915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
