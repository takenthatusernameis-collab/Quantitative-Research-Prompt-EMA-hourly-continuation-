# EMA Hourly Continuation — APT/USDT P34_89

**Symbol:** APT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.8442 |
| net_win_rate | 0.5218 |
| gross_profit_factor | 1.0835 |
| gross_win_rate | 0.5218 |
| sharpe_ratio | -1.0343 |
| sortino_ratio | -0.3024 |
| max_drawdown | 0.3463 |
| cagr | -0.1317 |
| net_avg_win | 75.2384 |
| net_avg_loss | -97.2706 |
| avg_hold_time_bars | 10.5146 |
| exposure | 0.1969 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
