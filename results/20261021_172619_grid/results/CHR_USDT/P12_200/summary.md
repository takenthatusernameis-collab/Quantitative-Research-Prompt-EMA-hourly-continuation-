# EMA Hourly Continuation — CHR/USDT P12_200

**Symbol:** CHR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.8234 |
| net_win_rate | 0.4911 |
| gross_profit_factor | 0.9525 |
| gross_win_rate | 0.4911 |
| sharpe_ratio | -0.9432 |
| sortino_ratio | -0.2253 |
| max_drawdown | 0.2867 |
| cagr | -0.1002 |
| net_avg_win | 79.0343 |
| net_avg_loss | -92.6258 |
| avg_hold_time_bars | 60.6157 |
| exposure | 0.7708 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
