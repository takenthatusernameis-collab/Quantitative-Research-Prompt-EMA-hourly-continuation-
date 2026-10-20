# EMA Hourly Continuation — CARV/USDT P8_200

**Symbol:** CARV/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.6431 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.9531 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -3.2255 |
| sortino_ratio | -1.0474 |
| max_drawdown | 0.6568 |
| cagr | -0.3898 |
| net_avg_win | 55.8917 |
| net_avg_loss | -78.8015 |
| avg_hold_time_bars | 29.9697 |
| exposure | 0.7235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
