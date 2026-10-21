# EMA Hourly Continuation — SOL/USDT P8_50

**Symbol:** SOL/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.7765 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0268 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -2.2957 |
| sortino_ratio | -0.8601 |
| max_drawdown | 0.6446 |
| cagr | -0.3277 |
| net_avg_win | 63.5552 |
| net_avg_loss | -83.2955 |
| avg_hold_time_bars | 12.3655 |
| exposure | 0.3845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
