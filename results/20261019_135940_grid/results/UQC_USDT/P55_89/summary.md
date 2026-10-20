# EMA Hourly Continuation — UQC/USDT P55_89

**Symbol:** UQC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.1532 |
| net_win_rate | 0.2188 |
| gross_profit_factor | 0.4365 |
| gross_win_rate | 0.2656 |
| sharpe_ratio | -10.3446 |
| sortino_ratio | -3.0291 |
| max_drawdown | 0.9856 |
| cagr | -0.8138 |
| net_avg_win | 21.2198 |
| net_avg_loss | -38.7947 |
| avg_hold_time_bars | 19.2943 |
| exposure | 0.3353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
