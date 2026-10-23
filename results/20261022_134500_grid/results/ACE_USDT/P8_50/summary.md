# EMA Hourly Continuation — ACE/USDT P8_50

**Symbol:** ACE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 816 |
| net_profit_factor | 0.6259 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.9508 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -4.1250 |
| sortino_ratio | -1.6548 |
| max_drawdown | 0.8641 |
| cagr | -0.5440 |
| net_avg_win | 36.7897 |
| net_avg_loss | -54.3452 |
| avg_hold_time_bars | 13.1998 |
| exposure | 0.4874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
