# EMA Hourly Continuation — SUN/USDT P8_20

**Symbol:** SUN/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 700 |
| net_profit_factor | 0.4287 |
| net_win_rate | 0.4443 |
| gross_profit_factor | 0.8826 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -7.6852 |
| sortino_ratio | -2.9354 |
| max_drawdown | 0.9717 |
| cagr | -0.7560 |
| net_avg_win | 23.4398 |
| net_avg_loss | -43.7140 |
| avg_hold_time_bars | 6.6971 |
| exposure | 0.2121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
