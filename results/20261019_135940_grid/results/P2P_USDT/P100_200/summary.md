# EMA Hourly Continuation — P2P/USDT P100_200

**Symbol:** P2P/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.5657 |
| net_win_rate | 0.4354 |
| gross_profit_factor | 0.7527 |
| gross_win_rate | 0.4354 |
| sharpe_ratio | -3.1092 |
| sortino_ratio | -0.8214 |
| max_drawdown | 0.6400 |
| cagr | -0.3261 |
| net_avg_win | 52.8492 |
| net_avg_loss | -72.0428 |
| avg_hold_time_bars | 10.8764 |
| exposure | 0.1760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
