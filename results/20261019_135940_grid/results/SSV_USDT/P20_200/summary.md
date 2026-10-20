# EMA Hourly Continuation — SSV/USDT P20_200

**Symbol:** SSV/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.6734 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9158 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -2.3602 |
| sortino_ratio | -0.6328 |
| max_drawdown | 0.5657 |
| cagr | -0.2569 |
| net_avg_win | 63.2111 |
| net_avg_loss | -84.9696 |
| avg_hold_time_bars | 40.9779 |
| exposure | 0.6713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
