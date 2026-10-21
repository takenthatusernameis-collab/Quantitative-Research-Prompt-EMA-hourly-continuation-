# EMA Hourly Continuation — AIOZ/USDT P34_55

**Symbol:** AIOZ/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.6917 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.8908 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -2.1472 |
| sortino_ratio | -0.5352 |
| max_drawdown | 0.4872 |
| cagr | -0.2178 |
| net_avg_win | 72.2386 |
| net_avg_loss | -91.6222 |
| avg_hold_time_bars | 6.6503 |
| exposure | 0.0925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
