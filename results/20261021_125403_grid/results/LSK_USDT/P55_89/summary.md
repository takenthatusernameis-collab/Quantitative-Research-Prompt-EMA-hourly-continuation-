# EMA Hourly Continuation — LSK/USDT P55_89

**Symbol:** LSK/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.6438 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9698 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.5545 |
| sortino_ratio | -0.7369 |
| max_drawdown | 0.5886 |
| cagr | -0.2869 |
| net_avg_win | 51.2152 |
| net_avg_loss | -79.5460 |
| avg_hold_time_bars | 6.2921 |
| exposure | 0.1155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
