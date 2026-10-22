# EMA Hourly Continuation — EWT/USDT P12_26

**Symbol:** EWT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.4991 |
| net_win_rate | 0.4006 |
| gross_profit_factor | 0.6908 |
| gross_win_rate | 0.4006 |
| sharpe_ratio | -4.1097 |
| sortino_ratio | -1.0545 |
| max_drawdown | 0.7136 |
| cagr | -0.3879 |
| net_avg_win | 53.8914 |
| net_avg_loss | -72.1661 |
| avg_hold_time_bars | 7.1896 |
| exposure | 0.1069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
