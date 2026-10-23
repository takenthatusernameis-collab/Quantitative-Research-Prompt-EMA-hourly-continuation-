# EMA Hourly Continuation — ELON/USDT P21_89

**Symbol:** ELON/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 773 |
| net_profit_factor | 0.4800 |
| net_win_rate | 0.4230 |
| gross_profit_factor | 0.7653 |
| gross_win_rate | 0.4282 |
| sharpe_ratio | -6.5645 |
| sortino_ratio | -2.5699 |
| max_drawdown | 0.9577 |
| cagr | -0.7125 |
| net_avg_win | 26.9957 |
| net_avg_loss | -41.2346 |
| avg_hold_time_bars | 9.3687 |
| exposure | 0.3292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
