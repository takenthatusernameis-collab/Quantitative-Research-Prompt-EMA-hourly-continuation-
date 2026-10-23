# EMA Hourly Continuation — MOG/USDT P12_100

**Symbol:** MOG/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.7530 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.9491 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -2.8099 |
| sortino_ratio | -1.0284 |
| max_drawdown | 0.7246 |
| cagr | -0.3848 |
| net_avg_win | 69.9272 |
| net_avg_loss | -83.9848 |
| avg_hold_time_bars | 18.6467 |
| exposure | 0.5719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
