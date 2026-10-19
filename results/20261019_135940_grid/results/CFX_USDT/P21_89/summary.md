# EMA Hourly Continuation — CFX/USDT P21_89

**Symbol:** CFX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.6132 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.9398 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -4.1037 |
| sortino_ratio | -1.4848 |
| max_drawdown | 0.8450 |
| cagr | -0.5111 |
| net_avg_win | 41.8413 |
| net_avg_loss | -61.7871 |
| avg_hold_time_bars | 12.9519 |
| exposure | 0.3915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
