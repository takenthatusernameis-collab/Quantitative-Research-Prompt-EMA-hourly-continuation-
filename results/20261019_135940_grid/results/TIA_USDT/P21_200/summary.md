# EMA Hourly Continuation — TIA/USDT P21_200

**Symbol:** TIA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.7053 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.8941 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -1.9358 |
| sortino_ratio | -0.4841 |
| max_drawdown | 0.4663 |
| cagr | -0.2019 |
| net_avg_win | 69.9223 |
| net_avg_loss | -89.4712 |
| avg_hold_time_bars | 47.5417 |
| exposure | 0.6742 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
