# EMA Hourly Continuation — W/USDT P21_200

**Symbol:** W/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.8193 |
| net_win_rate | 0.5143 |
| gross_profit_factor | 1.0628 |
| gross_win_rate | 0.5169 |
| sharpe_ratio | -1.2582 |
| sortino_ratio | -0.3491 |
| max_drawdown | 0.4465 |
| cagr | -0.1546 |
| net_avg_win | 78.7704 |
| net_avg_loss | -101.8036 |
| avg_hold_time_bars | 36.5455 |
| exposure | 0.6395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
