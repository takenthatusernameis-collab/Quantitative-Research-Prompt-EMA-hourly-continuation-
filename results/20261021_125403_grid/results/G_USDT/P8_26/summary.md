# EMA Hourly Continuation — G/USDT P8_26

**Symbol:** G/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 736 |
| net_profit_factor | 0.6417 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9417 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -3.9804 |
| sortino_ratio | -1.6665 |
| max_drawdown | 0.8108 |
| cagr | -0.5335 |
| net_avg_win | 40.2456 |
| net_avg_loss | -60.0487 |
| avg_hold_time_bars | 7.0584 |
| exposure | 0.2732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
