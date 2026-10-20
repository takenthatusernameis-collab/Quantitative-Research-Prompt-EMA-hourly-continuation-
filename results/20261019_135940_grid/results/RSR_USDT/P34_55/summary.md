# EMA Hourly Continuation — RSR/USDT P34_55

**Symbol:** RSR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 854 |
| net_profit_factor | 0.4309 |
| net_win_rate | 0.4297 |
| gross_profit_factor | 0.8183 |
| gross_win_rate | 0.4450 |
| sharpe_ratio | -7.7691 |
| sortino_ratio | -3.1957 |
| max_drawdown | 0.9825 |
| cagr | -0.8001 |
| net_avg_win | 20.2657 |
| net_avg_loss | -35.4457 |
| avg_hold_time_bars | 3.2658 |
| exposure | 0.1268 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
