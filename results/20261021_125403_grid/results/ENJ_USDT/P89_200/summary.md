# EMA Hourly Continuation — ENJ/USDT P89_200

**Symbol:** ENJ/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 0.8724 |
| net_win_rate | 0.5244 |
| gross_profit_factor | 1.0927 |
| gross_win_rate | 0.5244 |
| sharpe_ratio | -0.6317 |
| sortino_ratio | -0.1425 |
| max_drawdown | 0.1976 |
| cagr | -0.0653 |
| net_avg_win | 82.9913 |
| net_avg_loss | -104.8841 |
| avg_hold_time_bars | 21.0447 |
| exposure | 0.2343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
