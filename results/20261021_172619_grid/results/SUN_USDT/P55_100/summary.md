# EMA Hourly Continuation — SUN/USDT P55_100

**Symbol:** SUN/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.3829 |
| net_win_rate | 0.3840 |
| gross_profit_factor | 0.7264 |
| gross_win_rate | 0.4080 |
| sharpe_ratio | -6.3140 |
| sortino_ratio | -1.7555 |
| max_drawdown | 0.8853 |
| cagr | -0.5747 |
| net_avg_win | 38.0951 |
| net_avg_loss | -62.0281 |
| avg_hold_time_bars | 9.0240 |
| exposure | 0.1531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
