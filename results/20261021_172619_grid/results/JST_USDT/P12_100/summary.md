# EMA Hourly Continuation — JST/USDT P12_100

**Symbol:** JST/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.7062 |
| net_win_rate | 0.5193 |
| gross_profit_factor | 1.0562 |
| gross_win_rate | 0.5193 |
| sharpe_ratio | -1.9313 |
| sortino_ratio | -0.5434 |
| max_drawdown | 0.4973 |
| cagr | -0.2225 |
| net_avg_win | 55.9207 |
| net_avg_loss | -85.5387 |
| avg_hold_time_bars | 34.6710 |
| exposure | 0.6103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
