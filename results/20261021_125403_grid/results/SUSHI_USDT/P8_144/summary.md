# EMA Hourly Continuation — SUSHI/USDT P8_144

**Symbol:** SUSHI/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.8112 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 0.9925 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -1.3163 |
| sortino_ratio | -0.3825 |
| max_drawdown | 0.4070 |
| cagr | -0.1631 |
| net_avg_win | 75.1055 |
| net_avg_loss | -92.1379 |
| avg_hold_time_bars | 38.2410 |
| exposure | 0.7181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
