# EMA Hourly Continuation — LPT/USDT P12_55

**Symbol:** LPT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 984 |
| net_profit_factor | 0.5413 |
| net_win_rate | 0.4339 |
| gross_profit_factor | 0.8261 |
| gross_win_rate | 0.4461 |
| sharpe_ratio | -6.8337 |
| sortino_ratio | -3.0100 |
| max_drawdown | 0.9763 |
| cagr | -0.7692 |
| net_avg_win | 26.9431 |
| net_avg_loss | -38.1564 |
| avg_hold_time_bars | 9.1585 |
| exposure | 0.4096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
