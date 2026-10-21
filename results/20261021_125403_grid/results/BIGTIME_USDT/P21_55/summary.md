# EMA Hourly Continuation — BIGTIME/USDT P21_55

**Symbol:** BIGTIME/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.7185 |
| net_win_rate | 0.4871 |
| gross_profit_factor | 0.9366 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -2.4335 |
| sortino_ratio | -0.8084 |
| max_drawdown | 0.6164 |
| cagr | -0.3094 |
| net_avg_win | 58.6718 |
| net_avg_loss | -77.5484 |
| avg_hold_time_bars | 10.2085 |
| exposure | 0.2504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
