# EMA Hourly Continuation — BTT/USDT P12_50

**Symbol:** BTT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.5414 |
| net_win_rate | 0.4470 |
| gross_profit_factor | 0.8619 |
| gross_win_rate | 0.4488 |
| sharpe_ratio | -5.3598 |
| sortino_ratio | -1.8288 |
| max_drawdown | 0.8847 |
| cagr | -0.5764 |
| net_avg_win | 41.2594 |
| net_avg_loss | -61.6050 |
| avg_hold_time_bars | 14.6502 |
| exposure | 0.3769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
