# EMA Hourly Continuation — ACE/USDT P8_34

**Symbol:** ACE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.6704 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.8921 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -3.0344 |
| sortino_ratio | -1.1456 |
| max_drawdown | 0.7346 |
| cagr | -0.4090 |
| net_avg_win | 44.0794 |
| net_avg_loss | -61.0657 |
| avg_hold_time_bars | 10.8551 |
| exposure | 0.3458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
