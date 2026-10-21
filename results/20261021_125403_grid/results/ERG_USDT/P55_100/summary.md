# EMA Hourly Continuation — ERG/USDT P55_100

**Symbol:** ERG/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.5180 |
| net_win_rate | 0.4151 |
| gross_profit_factor | 0.6958 |
| gross_win_rate | 0.4151 |
| sharpe_ratio | -3.2020 |
| sortino_ratio | -0.7392 |
| max_drawdown | 0.5741 |
| cagr | -0.2882 |
| net_avg_win | 56.0915 |
| net_avg_loss | -76.8476 |
| avg_hold_time_bars | 11.5509 |
| exposure | 0.1391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
