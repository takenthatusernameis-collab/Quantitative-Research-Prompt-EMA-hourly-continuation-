# EMA Hourly Continuation — KAVA/USDT P55_89

**Symbol:** KAVA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.5079 |
| net_win_rate | 0.4332 |
| gross_profit_factor | 0.7926 |
| gross_win_rate | 0.4360 |
| sharpe_ratio | -4.4503 |
| sortino_ratio | -1.2166 |
| max_drawdown | 0.7789 |
| cagr | -0.4383 |
| net_avg_win | 49.6711 |
| net_avg_loss | -74.7534 |
| avg_hold_time_bars | 7.3488 |
| exposure | 0.1226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
