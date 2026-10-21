# EMA Hourly Continuation — TWT/USDT P12_34

**Symbol:** TWT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.6601 |
| net_win_rate | 0.5096 |
| gross_profit_factor | 0.9879 |
| gross_win_rate | 0.5096 |
| sharpe_ratio | -3.0476 |
| sortino_ratio | -1.1404 |
| max_drawdown | 0.7314 |
| cagr | -0.4052 |
| net_avg_win | 41.1410 |
| net_avg_loss | -64.7744 |
| avg_hold_time_bars | 6.7733 |
| exposure | 0.2078 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
