# EMA Hourly Continuation — KNC/USDT P100_200

**Symbol:** KNC/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.7954 |
| net_win_rate | 0.5273 |
| gross_profit_factor | 1.1143 |
| gross_win_rate | 0.5273 |
| sharpe_ratio | -1.1966 |
| sortino_ratio | -0.2854 |
| max_drawdown | 0.3117 |
| cagr | -0.1240 |
| net_avg_win | 75.8075 |
| net_avg_loss | -106.3092 |
| avg_hold_time_bars | 13.1164 |
| exposure | 0.1640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
