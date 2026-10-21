# EMA Hourly Continuation — RAY/USDT P8_200

**Symbol:** RAY/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.8308 |
| net_win_rate | 0.4929 |
| gross_profit_factor | 0.9687 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -1.0627 |
| sortino_ratio | -0.2850 |
| max_drawdown | 0.3305 |
| cagr | -0.1249 |
| net_avg_win | 80.3815 |
| net_avg_loss | -94.0440 |
| avg_hold_time_bars | 47.0737 |
| exposure | 0.7553 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
