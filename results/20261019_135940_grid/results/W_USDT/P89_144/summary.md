# EMA Hourly Continuation — W/USDT P89_144

**Symbol:** W/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.5721 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9484 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -3.6176 |
| sortino_ratio | -1.1120 |
| max_drawdown | 0.7616 |
| cagr | -0.4254 |
| net_avg_win | 42.3881 |
| net_avg_loss | -70.8011 |
| avg_hold_time_bars | 5.0722 |
| exposure | 0.1118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
