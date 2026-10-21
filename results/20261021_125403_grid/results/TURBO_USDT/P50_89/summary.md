# EMA Hourly Continuation — TURBO/USDT P50_89

**Symbol:** TURBO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.7609 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9799 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -1.6252 |
| sortino_ratio | -0.4389 |
| max_drawdown | 0.3851 |
| cagr | -0.1827 |
| net_avg_win | 74.5692 |
| net_avg_loss | -96.6833 |
| avg_hold_time_bars | 6.7027 |
| exposure | 0.1082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
