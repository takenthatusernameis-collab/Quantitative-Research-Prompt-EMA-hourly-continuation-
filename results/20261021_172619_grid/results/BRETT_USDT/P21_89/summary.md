# EMA Hourly Continuation — BRETT/USDT P21_89

**Symbol:** BRETT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.7556 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8820 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -1.9413 |
| sortino_ratio | -0.5884 |
| max_drawdown | 0.4790 |
| cagr | -0.2385 |
| net_avg_win | 73.2269 |
| net_avg_loss | -85.0631 |
| avg_hold_time_bars | 16.9256 |
| exposure | 0.3502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
