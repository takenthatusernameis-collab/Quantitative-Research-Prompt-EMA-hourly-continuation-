# EMA Hourly Continuation — DOT/USDT P12_100

**Symbol:** DOT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.8976 |
| net_win_rate | 0.5287 |
| gross_profit_factor | 1.1071 |
| gross_win_rate | 0.5287 |
| sharpe_ratio | -0.6072 |
| sortino_ratio | -0.1753 |
| max_drawdown | 0.3267 |
| cagr | -0.0815 |
| net_avg_win | 79.4988 |
| net_avg_loss | -99.3414 |
| avg_hold_time_bars | 34.5661 |
| exposure | 0.6300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
