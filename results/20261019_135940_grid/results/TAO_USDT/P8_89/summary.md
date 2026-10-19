# EMA Hourly Continuation — TAO/USDT P8_89

**Symbol:** TAO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 726 |
| net_profit_factor | 0.7515 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 1.0385 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.9573 |
| sortino_ratio | -1.1254 |
| max_drawdown | 0.7619 |
| cagr | -0.4147 |
| net_avg_win | 62.6303 |
| net_avg_loss | -80.6337 |
| avg_hold_time_bars | 19.0868 |
| exposure | 0.6299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
