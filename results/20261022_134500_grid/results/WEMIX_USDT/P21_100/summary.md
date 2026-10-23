# EMA Hourly Continuation — WEMIX/USDT P21_100

**Symbol:** WEMIX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1017 |
| net_profit_factor | 0.2959 |
| net_win_rate | 0.3156 |
| gross_profit_factor | 0.5010 |
| gross_win_rate | 0.3274 |
| sharpe_ratio | -12.4726 |
| sortino_ratio | -5.6866 |
| max_drawdown | 0.9992 |
| cagr | -0.9417 |
| net_avg_win | 13.0809 |
| net_avg_loss | -20.3894 |
| avg_hold_time_bars | 10.2301 |
| exposure | 0.4729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
