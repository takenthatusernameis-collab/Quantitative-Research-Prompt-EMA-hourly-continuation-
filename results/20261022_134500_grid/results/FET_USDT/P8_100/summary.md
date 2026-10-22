# EMA Hourly Continuation — FET/USDT P8_100

**Symbol:** FET/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.6915 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9370 |
| gross_win_rate | 0.4907 |
| sharpe_ratio | -2.6580 |
| sortino_ratio | -0.9044 |
| max_drawdown | 0.6778 |
| cagr | -0.3542 |
| net_avg_win | 51.8763 |
| net_avg_loss | -71.3041 |
| avg_hold_time_bars | 25.2978 |
| exposure | 0.6796 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
