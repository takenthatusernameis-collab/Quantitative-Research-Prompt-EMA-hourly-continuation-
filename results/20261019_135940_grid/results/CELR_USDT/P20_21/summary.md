# EMA Hourly Continuation — CELR/USDT P20_21

**Symbol:** CELR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1223 |
| net_profit_factor | 0.1371 |
| net_win_rate | 0.3099 |
| gross_profit_factor | 0.7586 |
| gross_win_rate | 0.4056 |
| sharpe_ratio | -16.3920 |
| sortino_ratio | -8.4703 |
| max_drawdown | 1.0000 |
| cagr | -0.9898 |
| net_avg_win | 4.1932 |
| net_avg_loss | -13.7312 |
| avg_hold_time_bars | 2.0515 |
| exposure | 0.1135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
