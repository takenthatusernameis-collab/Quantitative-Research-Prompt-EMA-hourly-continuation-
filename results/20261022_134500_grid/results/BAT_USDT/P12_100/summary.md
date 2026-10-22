# EMA Hourly Continuation — BAT/USDT P12_100

**Symbol:** BAT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.6240 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9783 |
| gross_win_rate | 0.4883 |
| sharpe_ratio | -3.8688 |
| sortino_ratio | -1.4279 |
| max_drawdown | 0.8291 |
| cagr | -0.4932 |
| net_avg_win | 41.5478 |
| net_avg_loss | -60.6449 |
| avg_hold_time_bars | 18.2245 |
| exposure | 0.5683 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
