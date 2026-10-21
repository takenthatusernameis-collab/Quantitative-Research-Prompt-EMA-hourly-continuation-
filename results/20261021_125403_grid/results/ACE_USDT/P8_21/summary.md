# EMA Hourly Continuation — ACE/USDT P8_21

**Symbol:** ACE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.6781 |
| net_win_rate | 0.4911 |
| gross_profit_factor | 0.9780 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -3.2093 |
| sortino_ratio | -1.1922 |
| max_drawdown | 0.7478 |
| cagr | -0.4208 |
| net_avg_win | 47.4381 |
| net_avg_loss | -67.5212 |
| avg_hold_time_bars | 6.8462 |
| exposure | 0.2094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
