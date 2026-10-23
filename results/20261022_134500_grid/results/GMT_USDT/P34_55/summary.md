# EMA Hourly Continuation — GMT/USDT P34_55

**Symbol:** GMT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 893 |
| net_profit_factor | 0.4173 |
| net_win_rate | 0.4211 |
| gross_profit_factor | 0.8629 |
| gross_win_rate | 0.4390 |
| sharpe_ratio | -8.8712 |
| sortino_ratio | -3.7658 |
| max_drawdown | 0.9915 |
| cagr | -0.8477 |
| net_avg_win | 18.8741 |
| net_avg_loss | -32.8976 |
| avg_hold_time_bars | 3.2676 |
| exposure | 0.1326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
