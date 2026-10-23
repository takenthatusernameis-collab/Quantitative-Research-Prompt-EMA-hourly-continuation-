# EMA Hourly Continuation — BICO/USDT P21_50

**Symbol:** BICO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 932 |
| net_profit_factor | 0.4899 |
| net_win_rate | 0.4506 |
| gross_profit_factor | 0.8799 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -6.0243 |
| sortino_ratio | -2.6070 |
| max_drawdown | 0.9538 |
| cagr | -0.7061 |
| net_avg_win | 21.8097 |
| net_avg_loss | -36.5196 |
| avg_hold_time_bars | 5.3047 |
| exposure | 0.2247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
