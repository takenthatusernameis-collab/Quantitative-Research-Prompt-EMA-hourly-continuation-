# EMA Hourly Continuation — ENS/USDT P8_12

**Symbol:** ENS/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.6882 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 0.9771 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -1.7647 |
| sortino_ratio | -0.4148 |
| max_drawdown | 0.4125 |
| cagr | -0.1730 |
| net_avg_win | 62.0371 |
| net_avg_loss | -91.4977 |
| avg_hold_time_bars | 5.5522 |
| exposure | 0.0676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
