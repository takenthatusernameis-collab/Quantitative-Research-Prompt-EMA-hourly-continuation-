# EMA Hourly Continuation — NYM/USDT P12_34

**Symbol:** NYM/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.4914 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.8585 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -4.3972 |
| sortino_ratio | -1.3955 |
| max_drawdown | 0.8068 |
| cagr | -0.4759 |
| net_avg_win | 33.7097 |
| net_avg_loss | -59.7706 |
| avg_hold_time_bars | 11.7429 |
| exposure | 0.2637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
