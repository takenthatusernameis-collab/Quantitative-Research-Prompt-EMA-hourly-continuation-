# EMA Hourly Continuation — CFX/USDT P8_200

**Symbol:** CFX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.8300 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 0.9798 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -1.0342 |
| sortino_ratio | -0.2500 |
| max_drawdown | 0.3278 |
| cagr | -0.1098 |
| net_avg_win | 87.1450 |
| net_avg_loss | -102.8156 |
| avg_hold_time_bars | 61.6899 |
| exposure | 0.8048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
