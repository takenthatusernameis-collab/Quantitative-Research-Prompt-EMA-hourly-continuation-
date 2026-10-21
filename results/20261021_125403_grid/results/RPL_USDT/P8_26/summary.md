# EMA Hourly Continuation — RPL/USDT P8_26

**Symbol:** RPL/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 860 |
| net_profit_factor | 0.7986 |
| net_win_rate | 0.5140 |
| gross_profit_factor | 1.0955 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -2.4513 |
| sortino_ratio | -1.0308 |
| max_drawdown | 0.7009 |
| cagr | -0.3778 |
| net_avg_win | 62.6109 |
| net_avg_loss | -82.9002 |
| avg_hold_time_bars | 6.7849 |
| exposure | 0.2641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
