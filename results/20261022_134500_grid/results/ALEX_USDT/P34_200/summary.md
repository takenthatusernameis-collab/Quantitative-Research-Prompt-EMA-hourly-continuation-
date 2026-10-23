# EMA Hourly Continuation — ALEX/USDT P34_200

**Symbol:** ALEX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.6504 |
| net_win_rate | 0.4452 |
| gross_profit_factor | 0.8574 |
| gross_win_rate | 0.4484 |
| sharpe_ratio | -2.6968 |
| sortino_ratio | -0.6666 |
| max_drawdown | 0.5820 |
| cagr | -0.2703 |
| net_avg_win | 73.7091 |
| net_avg_loss | -90.9303 |
| avg_hold_time_bars | 39.4968 |
| exposure | 0.5565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
