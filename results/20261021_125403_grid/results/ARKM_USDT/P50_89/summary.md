# EMA Hourly Continuation — ARKM/USDT P50_89

**Symbol:** ARKM/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.8141 |
| net_win_rate | 0.5102 |
| gross_profit_factor | 1.0526 |
| gross_win_rate | 0.5131 |
| sharpe_ratio | -1.2462 |
| sortino_ratio | -0.3314 |
| max_drawdown | 0.3611 |
| cagr | -0.1422 |
| net_avg_win | 80.0127 |
| net_avg_loss | -102.3775 |
| avg_hold_time_bars | 7.1166 |
| exposure | 0.1110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
