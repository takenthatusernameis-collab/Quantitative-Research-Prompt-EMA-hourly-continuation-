# EMA Hourly Continuation — CFG/USDT P12_21

**Symbol:** CFG/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.6550 |
| net_win_rate | 0.4715 |
| gross_profit_factor | 0.8765 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -2.2928 |
| sortino_ratio | -0.5973 |
| max_drawdown | 0.5016 |
| cagr | -0.2394 |
| net_avg_win | 60.0899 |
| net_avg_loss | -81.8420 |
| avg_hold_time_bars | 4.8769 |
| exposure | 0.0738 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
