# EMA Hourly Continuation — CSPR/USDT P8_55

**Symbol:** CSPR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1370 |
| net_profit_factor | 0.3965 |
| net_win_rate | 0.4080 |
| gross_profit_factor | 0.7360 |
| gross_win_rate | 0.4241 |
| sharpe_ratio | -9.4837 |
| sortino_ratio | -4.9249 |
| max_drawdown | 0.9977 |
| cagr | -0.9106 |
| net_avg_win | 11.7256 |
| net_avg_loss | -20.3839 |
| avg_hold_time_bars | 6.8883 |
| exposure | 0.4290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
