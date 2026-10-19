# EMA Hourly Continuation — NEO/USDT P26_89

**Symbol:** NEO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.4850 |
| net_win_rate | 0.4512 |
| gross_profit_factor | 0.8736 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -5.8769 |
| sortino_ratio | -2.1912 |
| max_drawdown | 0.9338 |
| cagr | -0.6576 |
| net_avg_win | 27.5237 |
| net_avg_loss | -46.6558 |
| avg_hold_time_bars | 10.3904 |
| exposure | 0.3339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
