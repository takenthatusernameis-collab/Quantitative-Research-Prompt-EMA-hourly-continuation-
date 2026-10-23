# EMA Hourly Continuation — ERG/USDT P55_200

**Symbol:** ERG/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.5048 |
| net_win_rate | 0.4273 |
| gross_profit_factor | 0.7579 |
| gross_win_rate | 0.4318 |
| sharpe_ratio | -4.4922 |
| sortino_ratio | -1.3397 |
| max_drawdown | 0.8004 |
| cagr | -0.4736 |
| net_avg_win | 42.7184 |
| net_avg_loss | -63.1364 |
| avg_hold_time_bars | 16.7919 |
| exposure | 0.3412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
