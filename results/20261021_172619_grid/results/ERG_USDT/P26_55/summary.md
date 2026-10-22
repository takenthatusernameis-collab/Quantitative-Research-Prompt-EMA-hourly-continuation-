# EMA Hourly Continuation — ERG/USDT P26_55

**Symbol:** ERG/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.5567 |
| net_win_rate | 0.4338 |
| gross_profit_factor | 0.7636 |
| gross_win_rate | 0.4338 |
| sharpe_ratio | -3.4277 |
| sortino_ratio | -0.9190 |
| max_drawdown | 0.6672 |
| cagr | -0.3453 |
| net_avg_win | 53.4036 |
| net_avg_loss | -73.4969 |
| avg_hold_time_bars | 8.2986 |
| exposure | 0.1339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
