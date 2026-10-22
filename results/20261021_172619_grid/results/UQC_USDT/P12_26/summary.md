# EMA Hourly Continuation — UQC/USDT P12_26

**Symbol:** UQC/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.3460 |
| net_win_rate | 0.3142 |
| gross_profit_factor | 0.5838 |
| gross_win_rate | 0.3448 |
| sharpe_ratio | -5.4110 |
| sortino_ratio | -1.2299 |
| max_drawdown | 0.7784 |
| cagr | -0.4451 |
| net_avg_win | 49.9108 |
| net_avg_loss | -66.0816 |
| avg_hold_time_bars | 43.9157 |
| exposure | 0.5188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
