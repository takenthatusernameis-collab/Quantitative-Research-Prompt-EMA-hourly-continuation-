# EMA Hourly Continuation — UMA/USDT P100_144

**Symbol:** UMA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.6729 |
| net_win_rate | 0.5018 |
| gross_profit_factor | 0.9938 |
| gross_win_rate | 0.5018 |
| sharpe_ratio | -2.0184 |
| sortino_ratio | -0.4778 |
| max_drawdown | 0.4349 |
| cagr | -0.1957 |
| net_avg_win | 63.7211 |
| net_avg_loss | -95.3932 |
| avg_hold_time_bars | 7.8745 |
| exposure | 0.0970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
