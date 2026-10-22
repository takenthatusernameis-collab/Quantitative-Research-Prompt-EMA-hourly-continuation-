# EMA Hourly Continuation — ICP/USDT P89_200

**Symbol:** ICP/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.5369 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.8854 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -3.7886 |
| sortino_ratio | -1.0797 |
| max_drawdown | 0.7417 |
| cagr | -0.4106 |
| net_avg_win | 43.6984 |
| net_avg_loss | -72.1351 |
| avg_hold_time_bars | 10.3542 |
| exposure | 0.1953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
