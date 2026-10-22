# EMA Hourly Continuation — POL/USDT P20_89

**Symbol:** POL/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.5368 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.8977 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -4.6483 |
| sortino_ratio | -1.7362 |
| max_drawdown | 0.8870 |
| cagr | -0.5694 |
| net_avg_win | 30.2395 |
| net_avg_loss | -50.7639 |
| avg_hold_time_bars | 13.4923 |
| exposure | 0.4360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
