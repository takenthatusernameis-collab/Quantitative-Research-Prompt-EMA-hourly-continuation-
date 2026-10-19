# EMA Hourly Continuation — SUN/USDT P8_144

**Symbol:** SUN/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.4593 |
| net_win_rate | 0.4369 |
| gross_profit_factor | 0.8867 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -5.0304 |
| sortino_ratio | -1.4374 |
| max_drawdown | 0.8484 |
| cagr | -0.5248 |
| net_avg_win | 38.4677 |
| net_avg_loss | -64.9910 |
| avg_hold_time_bars | 39.0841 |
| exposure | 0.7570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
