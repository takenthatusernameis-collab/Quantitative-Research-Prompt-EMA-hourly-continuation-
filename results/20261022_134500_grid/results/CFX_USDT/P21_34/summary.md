# EMA Hourly Continuation — CFX/USDT P21_34

**Symbol:** CFX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1163 |
| net_profit_factor | 0.3193 |
| net_win_rate | 0.3878 |
| gross_profit_factor | 0.7364 |
| gross_win_rate | 0.4153 |
| sharpe_ratio | -12.1435 |
| sortino_ratio | -5.8927 |
| max_drawdown | 0.9996 |
| cagr | -0.9534 |
| net_avg_win | 10.3980 |
| net_avg_loss | -20.6250 |
| avg_hold_time_bars | 2.6432 |
| exposure | 0.1397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
