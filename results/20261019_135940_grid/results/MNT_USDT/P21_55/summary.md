# EMA Hourly Continuation — MNT/USDT P21_55

**Symbol:** MNT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 868 |
| net_profit_factor | 0.3743 |
| net_win_rate | 0.4401 |
| gross_profit_factor | 0.8188 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -8.1732 |
| sortino_ratio | -3.3888 |
| max_drawdown | 0.9875 |
| cagr | -0.8226 |
| net_avg_win | 15.4531 |
| net_avg_loss | -32.4550 |
| avg_hold_time_bars | 6.3848 |
| exposure | 0.2519 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
