# EMA Hourly Continuation — AXS/USDT P144_200

**Symbol:** AXS/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.4781 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9910 |
| gross_win_rate | 0.5040 |
| sharpe_ratio | -4.2193 |
| sortino_ratio | -1.1275 |
| max_drawdown | 0.7762 |
| cagr | -0.4414 |
| net_avg_win | 39.4036 |
| net_avg_loss | -76.8330 |
| avg_hold_time_bars | 3.7925 |
| exposure | 0.0637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
