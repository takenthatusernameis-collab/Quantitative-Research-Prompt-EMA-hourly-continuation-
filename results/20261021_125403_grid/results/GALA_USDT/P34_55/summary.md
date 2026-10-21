# EMA Hourly Continuation — GALA/USDT P34_55

**Symbol:** GALA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.6094 |
| net_win_rate | 0.4485 |
| gross_profit_factor | 0.8216 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -2.9078 |
| sortino_ratio | -0.7527 |
| max_drawdown | 0.5949 |
| cagr | -0.2919 |
| net_avg_win | 61.1170 |
| net_avg_loss | -81.5555 |
| avg_hold_time_bars | 5.3030 |
| exposure | 0.0795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
