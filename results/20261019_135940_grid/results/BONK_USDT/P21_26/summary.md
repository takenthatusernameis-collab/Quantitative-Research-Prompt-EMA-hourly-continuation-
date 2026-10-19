# EMA Hourly Continuation — BONK/USDT P21_26

**Symbol:** BONK/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1173 |
| net_profit_factor | 0.3089 |
| net_win_rate | 0.3564 |
| gross_profit_factor | 0.7214 |
| gross_win_rate | 0.3905 |
| sharpe_ratio | -13.9003 |
| sortino_ratio | -6.8841 |
| max_drawdown | 0.9999 |
| cagr | -0.9748 |
| net_avg_win | 10.6924 |
| net_avg_loss | -19.1635 |
| avg_hold_time_bars | 1.8781 |
| exposure | 0.1001 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
