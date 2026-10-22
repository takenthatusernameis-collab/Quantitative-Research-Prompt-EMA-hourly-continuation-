# EMA Hourly Continuation — IOTX/USDT P34_100

**Symbol:** IOTX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.7653 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 0.9909 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -1.7568 |
| sortino_ratio | -0.5176 |
| max_drawdown | 0.4876 |
| cagr | -0.2116 |
| net_avg_win | 69.4721 |
| net_avg_loss | -90.3517 |
| avg_hold_time_bars | 13.2246 |
| exposure | 0.2543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
