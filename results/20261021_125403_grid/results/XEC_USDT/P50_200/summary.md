# EMA Hourly Continuation — XEC/USDT P50_200

**Symbol:** XEC/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.7325 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9454 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -1.6951 |
| sortino_ratio | -0.4304 |
| max_drawdown | 0.4373 |
| cagr | -0.1799 |
| net_avg_win | 69.5546 |
| net_avg_loss | -90.2936 |
| avg_hold_time_bars | 28.7138 |
| exposure | 0.4132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
