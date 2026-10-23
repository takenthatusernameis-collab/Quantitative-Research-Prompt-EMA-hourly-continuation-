# EMA Hourly Continuation — ACE/USDT P50_144

**Symbol:** ACE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.6748 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.9214 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -2.6585 |
| sortino_ratio | -0.7788 |
| max_drawdown | 0.6111 |
| cagr | -0.3032 |
| net_avg_win | 61.7397 |
| net_avg_loss | -81.3716 |
| avg_hold_time_bars | 14.9532 |
| exposure | 0.2889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
