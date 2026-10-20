# EMA Hourly Continuation — EUL/USDT P20_34

**Symbol:** EUL/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1054 |
| net_profit_factor | 0.2672 |
| net_win_rate | 0.3937 |
| gross_profit_factor | 0.5372 |
| gross_win_rate | 0.4137 |
| sharpe_ratio | -10.3463 |
| sortino_ratio | -4.7596 |
| max_drawdown | 0.9976 |
| cagr | -0.9089 |
| net_avg_win | 8.7653 |
| net_avg_loss | -21.3039 |
| avg_hold_time_bars | 3.4744 |
| exposure | 0.1665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
