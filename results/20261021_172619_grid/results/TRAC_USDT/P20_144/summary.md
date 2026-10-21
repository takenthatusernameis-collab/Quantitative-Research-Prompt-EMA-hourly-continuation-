# EMA Hourly Continuation — TRAC/USDT P20_144

**Symbol:** TRAC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.8460 |
| net_win_rate | 0.5071 |
| gross_profit_factor | 1.0304 |
| gross_win_rate | 0.5071 |
| sharpe_ratio | -1.0754 |
| sortino_ratio | -0.3176 |
| max_drawdown | 0.3282 |
| cagr | -0.1376 |
| net_avg_win | 79.3663 |
| net_avg_loss | -96.5038 |
| avg_hold_time_bars | 25.6934 |
| exposure | 0.4952 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
