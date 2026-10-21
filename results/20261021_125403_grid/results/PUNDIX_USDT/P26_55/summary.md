# EMA Hourly Continuation — PUNDIX/USDT P26_55

**Symbol:** PUNDIX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 546 |
| net_profit_factor | 0.6769 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 1.0072 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -3.1219 |
| sortino_ratio | -1.0474 |
| max_drawdown | 0.7145 |
| cagr | -0.3797 |
| net_avg_win | 54.1985 |
| net_avg_loss | -78.3330 |
| avg_hold_time_bars | 7.5256 |
| exposure | 0.1868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
