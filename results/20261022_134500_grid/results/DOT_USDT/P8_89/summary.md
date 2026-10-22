# EMA Hourly Continuation — DOT/USDT P8_89

**Symbol:** DOT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.6391 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 1.0186 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -3.4600 |
| sortino_ratio | -1.2166 |
| max_drawdown | 0.7873 |
| cagr | -0.4499 |
| net_avg_win | 43.9571 |
| net_avg_loss | -67.2791 |
| avg_hold_time_bars | 23.4613 |
| exposure | 0.6750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
