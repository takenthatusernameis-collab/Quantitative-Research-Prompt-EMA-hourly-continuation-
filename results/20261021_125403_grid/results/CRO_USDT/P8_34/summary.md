# EMA Hourly Continuation — CRO/USDT P8_34

**Symbol:** CRO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 759 |
| net_profit_factor | 0.6002 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.8840 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -4.4599 |
| sortino_ratio | -1.7557 |
| max_drawdown | 0.8744 |
| cagr | -0.5551 |
| net_avg_win | 36.5460 |
| net_avg_loss | -54.0770 |
| avg_hold_time_bars | 8.1621 |
| exposure | 0.2816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
