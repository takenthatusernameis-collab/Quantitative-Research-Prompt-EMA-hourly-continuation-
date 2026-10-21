# EMA Hourly Continuation — BSV/USDT P21_200

**Symbol:** BSV/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.6330 |
| net_win_rate | 0.4405 |
| gross_profit_factor | 0.7922 |
| gross_win_rate | 0.4405 |
| sharpe_ratio | -2.6809 |
| sortino_ratio | -0.6944 |
| max_drawdown | 0.5576 |
| cagr | -0.2735 |
| net_avg_win | 64.3047 |
| net_avg_loss | -79.9697 |
| avg_hold_time_bars | 41.3423 |
| exposure | 0.6314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
