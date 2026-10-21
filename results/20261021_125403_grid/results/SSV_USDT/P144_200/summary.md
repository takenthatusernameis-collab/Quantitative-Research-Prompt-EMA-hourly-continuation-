# EMA Hourly Continuation — SSV/USDT P144_200

**Symbol:** SSV/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.8075 |
| net_win_rate | 0.5145 |
| gross_profit_factor | 1.0691 |
| gross_win_rate | 0.5145 |
| sharpe_ratio | -1.0973 |
| sortino_ratio | -0.2446 |
| max_drawdown | 0.3427 |
| cagr | -0.1067 |
| net_avg_win | 83.8119 |
| net_avg_loss | -110.0027 |
| avg_hold_time_bars | 6.3900 |
| exposure | 0.0697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
