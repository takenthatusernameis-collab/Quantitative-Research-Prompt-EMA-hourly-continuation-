# EMA Hourly Continuation — POPCAT/USDT P55_200

**Symbol:** POPCAT/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.8021 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9381 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -1.1863 |
| sortino_ratio | -0.2972 |
| max_drawdown | 0.2946 |
| cagr | -0.1292 |
| net_avg_win | 81.2132 |
| net_avg_loss | -95.3324 |
| avg_hold_time_bars | 27.5150 |
| exposure | 0.3866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
