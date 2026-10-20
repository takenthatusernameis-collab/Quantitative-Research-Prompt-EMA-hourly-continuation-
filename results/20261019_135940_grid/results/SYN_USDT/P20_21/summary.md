# EMA Hourly Continuation — SYN/USDT P20_21

**Symbol:** SYN/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1190 |
| net_profit_factor | 0.1927 |
| net_win_rate | 0.3252 |
| gross_profit_factor | 0.6169 |
| gross_win_rate | 0.3866 |
| sharpe_ratio | -15.7139 |
| sortino_ratio | -7.9394 |
| max_drawdown | 1.0000 |
| cagr | -0.9874 |
| net_avg_win | 6.1664 |
| net_avg_loss | -15.4249 |
| avg_hold_time_bars | 1.9941 |
| exposure | 0.1079 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
