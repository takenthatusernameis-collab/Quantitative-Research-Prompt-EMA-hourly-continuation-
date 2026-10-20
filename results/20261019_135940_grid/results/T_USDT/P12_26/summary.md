# EMA Hourly Continuation — T/USDT P12_26

**Symbol:** T/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1071 |
| net_profit_factor | 0.4706 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.9815 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -8.3783 |
| sortino_ratio | -3.8691 |
| max_drawdown | 0.9919 |
| cagr | -0.8513 |
| net_avg_win | 18.2135 |
| net_avg_loss | -31.9144 |
| avg_hold_time_bars | 4.6228 |
| exposure | 0.2240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
