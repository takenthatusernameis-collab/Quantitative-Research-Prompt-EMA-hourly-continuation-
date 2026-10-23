# EMA Hourly Continuation — SUSHI/USDT P8_20

**Symbol:** SUSHI/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1676 |
| net_profit_factor | 0.3886 |
| net_win_rate | 0.4242 |
| gross_profit_factor | 0.8997 |
| gross_win_rate | 0.4499 |
| sharpe_ratio | -11.9046 |
| sortino_ratio | -6.8744 |
| max_drawdown | 0.9998 |
| cagr | -0.9678 |
| net_avg_win | 8.9374 |
| net_avg_loss | -16.9459 |
| avg_hold_time_bars | 2.9916 |
| exposure | 0.2269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
