# EMA Hourly Continuation — UMA/USDT P26_34

**Symbol:** UMA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.5757 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 0.9138 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -3.2030 |
| sortino_ratio | -0.8191 |
| max_drawdown | 0.6168 |
| cagr | -0.3147 |
| net_avg_win | 55.0729 |
| net_avg_loss | -86.4937 |
| avg_hold_time_bars | 5.3050 |
| exposure | 0.0767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
