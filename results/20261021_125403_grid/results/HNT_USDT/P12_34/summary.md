# EMA Hourly Continuation — HNT/USDT P12_34

**Symbol:** HNT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.6325 |
| net_win_rate | 0.4542 |
| gross_profit_factor | 0.8167 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -3.2756 |
| sortino_ratio | -1.0991 |
| max_drawdown | 0.7174 |
| cagr | -0.3954 |
| net_avg_win | 48.8042 |
| net_avg_loss | -64.2162 |
| avg_hold_time_bars | 7.4847 |
| exposure | 0.1895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
