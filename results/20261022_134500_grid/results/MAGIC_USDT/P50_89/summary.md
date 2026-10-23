# EMA Hourly Continuation — MAGIC/USDT P50_89

**Symbol:** MAGIC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.5899 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 1.0049 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -4.5402 |
| sortino_ratio | -1.6300 |
| max_drawdown | 0.8609 |
| cagr | -0.5367 |
| net_avg_win | 40.6047 |
| net_avg_loss | -62.6270 |
| avg_hold_time_bars | 5.1792 |
| exposure | 0.1497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
