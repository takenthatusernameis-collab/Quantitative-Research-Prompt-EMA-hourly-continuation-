# EMA Hourly Continuation — BICO/USDT P21_55

**Symbol:** BICO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.6354 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.8462 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -3.4381 |
| sortino_ratio | -1.1988 |
| max_drawdown | 0.7541 |
| cagr | -0.4227 |
| net_avg_win | 47.4294 |
| net_avg_loss | -63.1593 |
| avg_hold_time_bars | 8.2850 |
| exposure | 0.2260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
