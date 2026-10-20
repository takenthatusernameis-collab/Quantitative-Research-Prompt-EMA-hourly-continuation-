# EMA Hourly Continuation — ACE/USDT P20_34

**Symbol:** ACE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 884 |
| net_profit_factor | 0.4176 |
| net_win_rate | 0.4593 |
| gross_profit_factor | 0.9243 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -6.7559 |
| sortino_ratio | -2.8444 |
| max_drawdown | 0.9683 |
| cagr | -0.7438 |
| net_avg_win | 17.0920 |
| net_avg_loss | -34.7640 |
| avg_hold_time_bars | 4.4152 |
| exposure | 0.1766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
