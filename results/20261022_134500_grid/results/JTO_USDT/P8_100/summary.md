# EMA Hourly Continuation — JTO/USDT P8_100

**Symbol:** JTO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.6632 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.8893 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -3.3527 |
| sortino_ratio | -1.2099 |
| max_drawdown | 0.7670 |
| cagr | -0.4362 |
| net_avg_win | 49.4083 |
| net_avg_loss | -64.1608 |
| avg_hold_time_bars | 22.0457 |
| exposure | 0.6584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
