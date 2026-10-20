# EMA Hourly Continuation — PEOPLE/USDT P8_89

**Symbol:** PEOPLE/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.6824 |
| net_win_rate | 0.4718 |
| gross_profit_factor | 0.9284 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -3.0575 |
| sortino_ratio | -1.0405 |
| max_drawdown | 0.7337 |
| cagr | -0.3880 |
| net_avg_win | 55.2805 |
| net_avg_loss | -72.3612 |
| avg_hold_time_bars | 25.4821 |
| exposure | 0.6746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
