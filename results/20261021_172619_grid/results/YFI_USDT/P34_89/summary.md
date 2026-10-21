# EMA Hourly Continuation — YFI/USDT P34_89

**Symbol:** YFI/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.6577 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 0.9654 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -3.3098 |
| sortino_ratio | -1.0531 |
| max_drawdown | 0.7448 |
| cagr | -0.3836 |
| net_avg_win | 56.9131 |
| net_avg_loss | -79.5181 |
| avg_hold_time_bars | 10.1972 |
| exposure | 0.2293 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
