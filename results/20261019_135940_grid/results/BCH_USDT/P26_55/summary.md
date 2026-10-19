# EMA Hourly Continuation — BCH/USDT P26_55

**Symbol:** BCH/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 898 |
| net_profit_factor | 0.3898 |
| net_win_rate | 0.4454 |
| gross_profit_factor | 0.8594 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -8.5796 |
| sortino_ratio | -3.6639 |
| max_drawdown | 0.9899 |
| cagr | -0.8376 |
| net_avg_win | 15.8057 |
| net_avg_loss | -32.5665 |
| avg_hold_time_bars | 4.7004 |
| exposure | 0.1919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
