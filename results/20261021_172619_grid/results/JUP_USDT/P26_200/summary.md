# EMA Hourly Continuation — JUP/USDT P26_200

**Symbol:** JUP/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.8337 |
| net_win_rate | 0.4937 |
| gross_profit_factor | 0.9673 |
| gross_win_rate | 0.4937 |
| sharpe_ratio | -1.0160 |
| sortino_ratio | -0.2575 |
| max_drawdown | 0.3269 |
| cagr | -0.1136 |
| net_avg_win | 83.9300 |
| net_avg_loss | -98.1585 |
| avg_hold_time_bars | 37.0443 |
| exposure | 0.5321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
