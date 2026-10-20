# EMA Hourly Continuation — T/USDT P12_34

**Symbol:** T/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 990 |
| net_profit_factor | 0.5388 |
| net_win_rate | 0.4657 |
| gross_profit_factor | 0.9992 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -6.9584 |
| sortino_ratio | -3.0516 |
| max_drawdown | 0.9779 |
| cagr | -0.7794 |
| net_avg_win | 24.7826 |
| net_avg_loss | -40.0828 |
| avg_hold_time_bars | 6.1162 |
| exposure | 0.2740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
