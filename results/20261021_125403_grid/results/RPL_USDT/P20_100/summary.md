# EMA Hourly Continuation — RPL/USDT P20_100

**Symbol:** RPL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.7973 |
| net_win_rate | 0.4899 |
| gross_profit_factor | 0.9838 |
| gross_win_rate | 0.4899 |
| sharpe_ratio | -1.7426 |
| sortino_ratio | -0.5521 |
| max_drawdown | 0.5265 |
| cagr | -0.2248 |
| net_avg_win | 77.0233 |
| net_avg_loss | -92.7718 |
| avg_hold_time_bars | 20.3968 |
| exposure | 0.4560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
