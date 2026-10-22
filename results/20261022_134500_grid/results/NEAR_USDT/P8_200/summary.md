# EMA Hourly Continuation — NEAR/USDT P8_200

**Symbol:** NEAR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.7291 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9482 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -1.7666 |
| sortino_ratio | -0.4429 |
| max_drawdown | 0.4666 |
| cagr | -0.1881 |
| net_avg_win | 72.1494 |
| net_avg_loss | -92.8421 |
| avg_hold_time_bars | 57.9140 |
| exposure | 0.8266 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
