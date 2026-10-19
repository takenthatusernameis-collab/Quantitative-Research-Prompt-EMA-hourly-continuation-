# EMA Hourly Continuation — NEO/USDT P21_89

**Symbol:** NEO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 730 |
| net_profit_factor | 0.5118 |
| net_win_rate | 0.4521 |
| gross_profit_factor | 0.8744 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -5.8675 |
| sortino_ratio | -2.2249 |
| max_drawdown | 0.9355 |
| cagr | -0.6616 |
| net_avg_win | 29.6830 |
| net_avg_loss | -47.8439 |
| avg_hold_time_bars | 11.4767 |
| exposure | 0.3808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
