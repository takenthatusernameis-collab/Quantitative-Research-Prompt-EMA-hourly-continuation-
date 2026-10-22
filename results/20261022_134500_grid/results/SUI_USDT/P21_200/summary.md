# EMA Hourly Continuation — SUI/USDT P21_200

**Symbol:** SUI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.6769 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.9490 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -2.3443 |
| sortino_ratio | -0.6267 |
| max_drawdown | 0.5630 |
| cagr | -0.2607 |
| net_avg_win | 64.0062 |
| net_avg_loss | -86.5979 |
| avg_hold_time_bars | 38.3984 |
| exposure | 0.6353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
