# EMA Hourly Continuation — ETC/USDT P21_26

**Symbol:** ETC/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 0.7027 |
| net_win_rate | 0.5389 |
| gross_profit_factor | 1.1490 |
| gross_win_rate | 0.5389 |
| sharpe_ratio | -1.3197 |
| sortino_ratio | -0.2475 |
| max_drawdown | 0.2441 |
| cagr | -0.1055 |
| net_avg_win | 64.1160 |
| net_avg_loss | -106.6423 |
| avg_hold_time_bars | 3.9162 |
| exposure | 0.0297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
