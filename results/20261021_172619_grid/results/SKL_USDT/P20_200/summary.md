# EMA Hourly Continuation — SKL/USDT P20_200

**Symbol:** SKL/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.8469 |
| net_win_rate | 0.5032 |
| gross_profit_factor | 0.9923 |
| gross_win_rate | 0.5032 |
| sharpe_ratio | -0.8513 |
| sortino_ratio | -0.2137 |
| max_drawdown | 0.3380 |
| cagr | -0.0955 |
| net_avg_win | 79.5619 |
| net_avg_loss | -95.1710 |
| avg_hold_time_bars | 44.2403 |
| exposure | 0.6194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
