# EMA Hourly Continuation — DODO/USDT P55_89

**Symbol:** DODO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 772 |
| net_profit_factor | 0.4931 |
| net_win_rate | 0.4210 |
| gross_profit_factor | 0.8836 |
| gross_win_rate | 0.4391 |
| sharpe_ratio | -7.2924 |
| sortino_ratio | -2.8539 |
| max_drawdown | 0.9715 |
| cagr | -0.7539 |
| net_avg_win | 29.0578 |
| net_avg_loss | -42.8471 |
| avg_hold_time_bars | 4.1295 |
| exposure | 0.1443 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
