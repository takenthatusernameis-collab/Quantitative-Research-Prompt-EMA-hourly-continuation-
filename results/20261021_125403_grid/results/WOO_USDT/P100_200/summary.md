# EMA Hourly Continuation — WOO/USDT P100_200

**Symbol:** WOO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.7199 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9267 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -1.6740 |
| sortino_ratio | -0.3979 |
| max_drawdown | 0.3737 |
| cagr | -0.1670 |
| net_avg_win | 70.6133 |
| net_avg_loss | -91.9097 |
| avg_hold_time_bars | 12.0289 |
| exposure | 0.1515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
