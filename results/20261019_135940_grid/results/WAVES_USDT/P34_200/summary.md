# EMA Hourly Continuation — WAVES/USDT P34_200

**Symbol:** WAVES/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.4987 |
| net_win_rate | 0.4401 |
| gross_profit_factor | 0.8285 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -4.7931 |
| sortino_ratio | -1.5373 |
| max_drawdown | 0.8583 |
| cagr | -0.5363 |
| net_avg_win | 36.1827 |
| net_avg_loss | -57.0272 |
| avg_hold_time_bars | 18.6348 |
| exposure | 0.4523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
