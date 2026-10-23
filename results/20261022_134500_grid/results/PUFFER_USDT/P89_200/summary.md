# EMA Hourly Continuation — PUFFER/USDT P89_200

**Symbol:** PUFFER/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.5553 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.7860 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -3.2943 |
| sortino_ratio | -0.8805 |
| max_drawdown | 0.5746 |
| cagr | -0.3398 |
| net_avg_win | 54.9028 |
| net_avg_loss | -79.2209 |
| avg_hold_time_bars | 12.7276 |
| exposure | 0.2089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
