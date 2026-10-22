# EMA Hourly Continuation — FLOKI/USDT P26_50

**Symbol:** FLOKI/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1045 |
| net_profit_factor | 0.4943 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 0.8354 |
| gross_win_rate | 0.4507 |
| sharpe_ratio | -8.4356 |
| sortino_ratio | -3.8250 |
| max_drawdown | 0.9930 |
| cagr | -0.8559 |
| net_avg_win | 21.0402 |
| net_avg_loss | -33.5999 |
| avg_hold_time_bars | 3.4287 |
| exposure | 0.1629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
