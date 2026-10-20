# EMA Hourly Continuation — BRETT/USDT P26_89

**Symbol:** BRETT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.6118 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.8413 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -4.3985 |
| sortino_ratio | -1.6120 |
| max_drawdown | 0.8367 |
| cagr | -0.5308 |
| net_avg_win | 46.2787 |
| net_avg_loss | -61.0292 |
| avg_hold_time_bars | 10.6242 |
| exposure | 0.3251 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
