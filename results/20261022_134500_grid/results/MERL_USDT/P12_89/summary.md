# EMA Hourly Continuation — MERL/USDT P12_89

**Symbol:** MERL/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.7308 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9727 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -2.9846 |
| sortino_ratio | -1.0786 |
| max_drawdown | 0.7580 |
| cagr | -0.4037 |
| net_avg_win | 62.1719 |
| net_avg_loss | -78.3964 |
| avg_hold_time_bars | 19.7700 |
| exposure | 0.5957 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
