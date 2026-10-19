# EMA Hourly Continuation — POL/USDT P12_26

**Symbol:** POL/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1475 |
| net_profit_factor | 0.3115 |
| net_win_rate | 0.3980 |
| gross_profit_factor | 0.7638 |
| gross_win_rate | 0.4271 |
| sharpe_ratio | -13.4276 |
| sortino_ratio | -7.3325 |
| max_drawdown | 0.9999 |
| cagr | -0.9773 |
| net_avg_win | 7.7087 |
| net_avg_loss | -16.3561 |
| avg_hold_time_bars | 2.8942 |
| exposure | 0.1940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
