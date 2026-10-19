# EMA Hourly Continuation — BCH/USDT P12_26

**Symbol:** BCH/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1340 |
| net_profit_factor | 0.2406 |
| net_win_rate | 0.3888 |
| gross_profit_factor | 0.7138 |
| gross_win_rate | 0.4299 |
| sharpe_ratio | -13.9329 |
| sortino_ratio | -7.3179 |
| max_drawdown | 0.9999 |
| cagr | -0.9794 |
| net_avg_win | 6.0821 |
| net_avg_loss | -16.0784 |
| avg_hold_time_bars | 2.8291 |
| exposure | 0.1723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
