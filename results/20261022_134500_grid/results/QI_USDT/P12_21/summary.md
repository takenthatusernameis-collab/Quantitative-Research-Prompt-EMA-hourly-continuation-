# EMA Hourly Continuation — QI/USDT P12_21

**Symbol:** QI/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1263 |
| net_profit_factor | 0.3169 |
| net_win_rate | 0.3919 |
| gross_profit_factor | 0.7212 |
| gross_win_rate | 0.4268 |
| sharpe_ratio | -12.0815 |
| sortino_ratio | -6.1159 |
| max_drawdown | 0.9996 |
| cagr | -0.9551 |
| net_avg_win | 9.3681 |
| net_avg_loss | -19.0537 |
| avg_hold_time_bars | 3.1473 |
| exposure | 0.1799 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
