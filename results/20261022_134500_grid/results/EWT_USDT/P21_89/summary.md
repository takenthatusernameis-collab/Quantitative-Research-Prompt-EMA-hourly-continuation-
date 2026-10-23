# EMA Hourly Continuation — EWT/USDT P21_89

**Symbol:** EWT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.4592 |
| net_win_rate | 0.4078 |
| gross_profit_factor | 0.7082 |
| gross_win_rate | 0.4172 |
| sharpe_ratio | -6.5839 |
| sortino_ratio | -2.5039 |
| max_drawdown | 0.9562 |
| cagr | -0.7097 |
| net_avg_win | 26.7671 |
| net_avg_loss | -40.1421 |
| avg_hold_time_bars | 9.3096 |
| exposure | 0.3144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
