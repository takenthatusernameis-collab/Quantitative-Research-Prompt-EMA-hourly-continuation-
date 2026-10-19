# EMA Hourly Continuation — WLD/USDT P8_200

**Symbol:** WLD/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.7674 |
| net_win_rate | 0.4983 |
| gross_profit_factor | 0.9941 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -1.4240 |
| sortino_ratio | -0.3485 |
| max_drawdown | 0.3894 |
| cagr | -0.1550 |
| net_avg_win | 75.3452 |
| net_avg_loss | -97.5366 |
| avg_hold_time_bars | 59.8878 |
| exposure | 0.8248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
