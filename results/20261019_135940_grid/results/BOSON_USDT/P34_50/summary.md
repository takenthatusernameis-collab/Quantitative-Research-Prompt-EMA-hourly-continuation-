# EMA Hourly Continuation — BOSON/USDT P34_50

**Symbol:** BOSON/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 868 |
| net_profit_factor | 0.3845 |
| net_win_rate | 0.4136 |
| gross_profit_factor | 0.7693 |
| gross_win_rate | 0.4366 |
| sharpe_ratio | -8.1021 |
| sortino_ratio | -3.3545 |
| max_drawdown | 0.9850 |
| cagr | -0.8123 |
| net_avg_win | 17.1403 |
| net_avg_loss | -31.4412 |
| avg_hold_time_bars | 3.3606 |
| exposure | 0.1326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
