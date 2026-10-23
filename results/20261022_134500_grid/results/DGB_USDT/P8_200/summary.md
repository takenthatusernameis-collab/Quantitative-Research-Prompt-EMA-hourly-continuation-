# EMA Hourly Continuation — DGB/USDT P8_200

**Symbol:** DGB/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.5997 |
| net_win_rate | 0.4381 |
| gross_profit_factor | 0.8447 |
| gross_win_rate | 0.4440 |
| sharpe_ratio | -4.1062 |
| sortino_ratio | -1.2976 |
| max_drawdown | 0.8026 |
| cagr | -0.4618 |
| net_avg_win | 53.0110 |
| net_avg_loss | -68.9192 |
| avg_hold_time_bars | 33.6444 |
| exposure | 0.7784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
