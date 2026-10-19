# EMA Hourly Continuation — POL/USDT P26_89

**Symbol:** POL/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.4943 |
| net_win_rate | 0.4702 |
| gross_profit_factor | 0.8496 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -5.0134 |
| sortino_ratio | -1.8346 |
| max_drawdown | 0.9018 |
| cagr | -0.5950 |
| net_avg_win | 27.1393 |
| net_avg_loss | -48.7160 |
| avg_hold_time_bars | 11.3930 |
| exposure | 0.3558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
