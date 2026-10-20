# EMA Hourly Continuation — ZEN/USDT P50_55

**Symbol:** ZEN/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 922 |
| net_profit_factor | 0.1781 |
| net_win_rate | 0.3492 |
| gross_profit_factor | 0.6633 |
| gross_win_rate | 0.4154 |
| sharpe_ratio | -12.9190 |
| sortino_ratio | -5.7111 |
| max_drawdown | 0.9996 |
| cagr | -0.9541 |
| net_avg_win | 6.7264 |
| net_avg_loss | -20.2692 |
| avg_hold_time_bars | 1.8134 |
| exposure | 0.0760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
