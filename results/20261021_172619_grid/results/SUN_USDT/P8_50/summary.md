# EMA Hourly Continuation — SUN/USDT P8_50

**Symbol:** SUN/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.5278 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.8737 |
| gross_win_rate | 0.4592 |
| sharpe_ratio | -5.8287 |
| sortino_ratio | -2.1254 |
| max_drawdown | 0.9240 |
| cagr | -0.6400 |
| net_avg_win | 34.6583 |
| net_avg_loss | -53.7592 |
| avg_hold_time_bars | 15.9607 |
| exposure | 0.4781 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
