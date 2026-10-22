# EMA Hourly Continuation — SKL/USDT P21_200

**Symbol:** SKL/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.8677 |
| net_win_rate | 0.5098 |
| gross_profit_factor | 1.0188 |
| gross_win_rate | 0.5098 |
| sharpe_ratio | -0.7162 |
| sortino_ratio | -0.1795 |
| max_drawdown | 0.3269 |
| cagr | -0.0817 |
| net_avg_win | 80.9861 |
| net_avg_loss | -97.0666 |
| avg_hold_time_bars | 45.0882 |
| exposure | 0.6271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
