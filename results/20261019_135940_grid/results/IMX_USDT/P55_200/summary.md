# EMA Hourly Continuation — IMX/USDT P55_200

**Symbol:** IMX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.8389 |
| net_win_rate | 0.5349 |
| gross_profit_factor | 1.1342 |
| gross_win_rate | 0.5349 |
| sharpe_ratio | -0.9299 |
| sortino_ratio | -0.2458 |
| max_drawdown | 0.2991 |
| cagr | -0.1109 |
| net_avg_win | 72.6438 |
| net_avg_loss | -99.5788 |
| avg_hold_time_bars | 26.0494 |
| exposure | 0.4055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
