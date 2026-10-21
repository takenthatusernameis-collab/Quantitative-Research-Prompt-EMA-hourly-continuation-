# EMA Hourly Continuation — AIOZ/USDT P55_89

**Symbol:** AIOZ/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.8325 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0666 |
| gross_win_rate | 0.5126 |
| sharpe_ratio | -1.1313 |
| sortino_ratio | -0.2899 |
| max_drawdown | 0.4084 |
| cagr | -0.1260 |
| net_avg_win | 87.4994 |
| net_avg_loss | -110.5248 |
| avg_hold_time_bars | 7.2453 |
| exposure | 0.1047 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
