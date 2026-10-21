# EMA Hourly Continuation — QI/USDT P100_200

**Symbol:** QI/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.6142 |
| net_win_rate | 0.4564 |
| gross_profit_factor | 0.8167 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -2.4751 |
| sortino_ratio | -0.6067 |
| max_drawdown | 0.5099 |
| cagr | -0.2426 |
| net_avg_win | 58.9839 |
| net_avg_loss | -80.6234 |
| avg_hold_time_bars | 11.5906 |
| exposure | 0.1563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
