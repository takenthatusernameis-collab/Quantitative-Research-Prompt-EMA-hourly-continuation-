# EMA Hourly Continuation — ACE/USDT P55_100

**Symbol:** ACE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.7864 |
| net_win_rate | 0.5140 |
| gross_profit_factor | 1.0627 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -1.4435 |
| sortino_ratio | -0.3906 |
| max_drawdown | 0.3988 |
| cagr | -0.1646 |
| net_avg_win | 73.3698 |
| net_avg_loss | -98.6940 |
| avg_hold_time_bars | 9.1404 |
| exposure | 0.1473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
