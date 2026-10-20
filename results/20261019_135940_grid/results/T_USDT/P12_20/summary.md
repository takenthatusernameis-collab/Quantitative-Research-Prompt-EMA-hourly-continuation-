# EMA Hourly Continuation — T/USDT P12_20

**Symbol:** T/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1119 |
| net_profit_factor | 0.3956 |
| net_win_rate | 0.4352 |
| gross_profit_factor | 0.9969 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -10.0838 |
| sortino_ratio | -4.7974 |
| max_drawdown | 0.9977 |
| cagr | -0.9093 |
| net_avg_win | 13.4059 |
| net_avg_loss | -26.1158 |
| avg_hold_time_bars | 3.7936 |
| exposure | 0.1921 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
