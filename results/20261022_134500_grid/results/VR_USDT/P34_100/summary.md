# EMA Hourly Continuation — VR/USDT P34_100

**Symbol:** VR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 713 |
| net_profit_factor | 0.5065 |
| net_win_rate | 0.3548 |
| gross_profit_factor | 0.8055 |
| gross_win_rate | 0.3675 |
| sharpe_ratio | -9.9329 |
| sortino_ratio | -3.6891 |
| max_drawdown | 0.9953 |
| cagr | -0.8810 |
| net_avg_win | 40.3798 |
| net_avg_loss | -43.8443 |
| avg_hold_time_bars | 8.8654 |
| exposure | 0.2873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
