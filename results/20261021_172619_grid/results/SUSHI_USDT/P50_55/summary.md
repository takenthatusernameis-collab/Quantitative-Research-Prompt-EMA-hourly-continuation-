# EMA Hourly Continuation — SUSHI/USDT P50_55

**Symbol:** SUSHI/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 128 |
| net_profit_factor | 0.7650 |
| net_win_rate | 0.5312 |
| gross_profit_factor | 1.1289 |
| gross_win_rate | 0.5312 |
| sharpe_ratio | -0.9429 |
| sortino_ratio | -0.1539 |
| max_drawdown | 0.2275 |
| cagr | -0.0679 |
| net_avg_win | 77.8050 |
| net_avg_loss | -115.2620 |
| avg_hold_time_bars | 5.0469 |
| exposure | 0.0292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
