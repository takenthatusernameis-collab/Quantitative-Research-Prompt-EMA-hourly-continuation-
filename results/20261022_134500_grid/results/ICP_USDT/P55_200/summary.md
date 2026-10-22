# EMA Hourly Continuation — ICP/USDT P55_200

**Symbol:** ICP/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.6415 |
| net_win_rate | 0.4960 |
| gross_profit_factor | 0.9843 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -2.6571 |
| sortino_ratio | -0.7262 |
| max_drawdown | 0.6007 |
| cagr | -0.2960 |
| net_avg_win | 55.7514 |
| net_avg_loss | -85.5443 |
| avg_hold_time_bars | 22.0923 |
| exposure | 0.3806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
