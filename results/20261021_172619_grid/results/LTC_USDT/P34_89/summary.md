# EMA Hourly Continuation — LTC/USDT P34_89

**Symbol:** LTC/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.5628 |
| net_win_rate | 0.4453 |
| gross_profit_factor | 0.8017 |
| gross_win_rate | 0.4453 |
| sharpe_ratio | -3.5077 |
| sortino_ratio | -0.9913 |
| max_drawdown | 0.7072 |
| cagr | -0.3663 |
| net_avg_win | 50.1702 |
| net_avg_loss | -71.5576 |
| avg_hold_time_bars | 12.0662 |
| exposure | 0.2155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
