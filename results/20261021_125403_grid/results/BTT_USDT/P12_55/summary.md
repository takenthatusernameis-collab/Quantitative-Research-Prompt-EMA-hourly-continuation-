# EMA Hourly Continuation — BTT/USDT P12_55

**Symbol:** BTT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 563 |
| net_profit_factor | 0.5737 |
| net_win_rate | 0.4565 |
| gross_profit_factor | 0.9114 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -5.0585 |
| sortino_ratio | -1.7198 |
| max_drawdown | 0.8729 |
| cagr | -0.5533 |
| net_avg_win | 45.4372 |
| net_avg_loss | -66.5212 |
| avg_hold_time_bars | 15.8739 |
| exposure | 0.4062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
