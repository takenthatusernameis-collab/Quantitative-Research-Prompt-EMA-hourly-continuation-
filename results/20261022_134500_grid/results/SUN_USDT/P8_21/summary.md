# EMA Hourly Continuation — SUN/USDT P8_21

**Symbol:** SUN/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1426 |
| net_profit_factor | 0.1414 |
| net_win_rate | 0.3696 |
| gross_profit_factor | 0.6052 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -15.8266 |
| sortino_ratio | -8.6894 |
| max_drawdown | 1.0000 |
| cagr | -0.9907 |
| net_avg_win | 3.1244 |
| net_avg_loss | -12.9549 |
| avg_hold_time_bars | 4.3647 |
| exposure | 0.2817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
