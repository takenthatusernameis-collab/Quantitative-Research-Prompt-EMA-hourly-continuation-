# EMA Hourly Continuation — PUNDIX/USDT P20_34

**Symbol:** PUNDIX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.5426 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.8535 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -4.2258 |
| sortino_ratio | -1.3321 |
| max_drawdown | 0.7913 |
| cagr | -0.4583 |
| net_avg_win | 41.7916 |
| net_avg_loss | -66.3125 |
| avg_hold_time_bars | 6.0104 |
| exposure | 0.1317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
