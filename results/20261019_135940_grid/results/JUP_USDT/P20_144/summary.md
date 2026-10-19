# EMA Hourly Continuation — JUP/USDT P20_144

**Symbol:** JUP/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.5723 |
| net_win_rate | 0.4438 |
| gross_profit_factor | 0.8180 |
| gross_win_rate | 0.4494 |
| sharpe_ratio | -4.0740 |
| sortino_ratio | -1.3328 |
| max_drawdown | 0.8056 |
| cagr | -0.4711 |
| net_avg_win | 44.3031 |
| net_avg_loss | -61.7797 |
| avg_hold_time_bars | 20.4899 |
| exposure | 0.5057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
