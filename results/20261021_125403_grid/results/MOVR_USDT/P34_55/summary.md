# EMA Hourly Continuation — MOVR/USDT P34_55

**Symbol:** MOVR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.8051 |
| net_win_rate | 0.5266 |
| gross_profit_factor | 1.1139 |
| gross_win_rate | 0.5266 |
| sharpe_ratio | -1.2791 |
| sortino_ratio | -0.3489 |
| max_drawdown | 0.3887 |
| cagr | -0.1482 |
| net_avg_win | 72.8700 |
| net_avg_loss | -100.6816 |
| avg_hold_time_bars | 5.5322 |
| exposure | 0.0898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
