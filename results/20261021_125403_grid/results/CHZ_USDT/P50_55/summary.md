# EMA Hourly Continuation — CHZ/USDT P50_55

**Symbol:** CHZ/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 102 |
| net_profit_factor | 0.6523 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.9423 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -1.3969 |
| sortino_ratio | -0.2023 |
| max_drawdown | 0.2565 |
| cagr | -0.0890 |
| net_avg_win | 79.8876 |
| net_avg_loss | -113.2209 |
| avg_hold_time_bars | 4.0294 |
| exposure | 0.0187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
