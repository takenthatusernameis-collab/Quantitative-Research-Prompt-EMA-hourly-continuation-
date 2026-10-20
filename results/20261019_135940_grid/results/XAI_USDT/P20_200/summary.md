# EMA Hourly Continuation — XAI/USDT P20_200

**Symbol:** XAI/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.7206 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9577 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -1.8449 |
| sortino_ratio | -0.4444 |
| max_drawdown | 0.4580 |
| cagr | -0.1879 |
| net_avg_win | 75.5028 |
| net_avg_loss | -97.1001 |
| avg_hold_time_bars | 57.2907 |
| exposure | 0.7526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
