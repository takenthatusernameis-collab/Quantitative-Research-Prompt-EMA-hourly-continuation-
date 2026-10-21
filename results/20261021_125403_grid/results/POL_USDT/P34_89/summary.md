# EMA Hourly Continuation — POL/USDT P34_89

**Symbol:** POL/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.7232 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 0.9651 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -1.8269 |
| sortino_ratio | -0.5429 |
| max_drawdown | 0.4796 |
| cagr | -0.2203 |
| net_avg_win | 56.4715 |
| net_avg_loss | -78.4469 |
| avg_hold_time_bars | 11.8904 |
| exposure | 0.2319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
