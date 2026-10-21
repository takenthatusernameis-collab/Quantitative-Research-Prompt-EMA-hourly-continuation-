# EMA Hourly Continuation — ETH/USDT P34_50

**Symbol:** ETH/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 210 |
| net_profit_factor | 0.5980 |
| net_win_rate | 0.5095 |
| gross_profit_factor | 1.0084 |
| gross_win_rate | 0.5095 |
| sharpe_ratio | -2.1708 |
| sortino_ratio | -0.4521 |
| max_drawdown | 0.4114 |
| cagr | -0.1883 |
| net_avg_win | 56.6879 |
| net_avg_loss | -98.4829 |
| avg_hold_time_bars | 6.2190 |
| exposure | 0.0594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
