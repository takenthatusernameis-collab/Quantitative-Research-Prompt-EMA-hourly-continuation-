# EMA Hourly Continuation — SUSHI/USDT P8_34

**Symbol:** SUSHI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1352 |
| net_profit_factor | 0.5209 |
| net_win_rate | 0.4564 |
| gross_profit_factor | 0.9485 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -8.0087 |
| sortino_ratio | -4.1174 |
| max_drawdown | 0.9939 |
| cagr | -0.8677 |
| net_avg_win | 17.5149 |
| net_avg_loss | -28.2258 |
| avg_hold_time_bars | 5.7633 |
| exposure | 0.3526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
