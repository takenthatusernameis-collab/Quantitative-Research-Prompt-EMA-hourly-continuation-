# EMA Hourly Continuation — TFUEL/USDT P26_55

**Symbol:** TFUEL/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.3908 |
| net_win_rate | 0.3951 |
| gross_profit_factor | 0.7384 |
| gross_win_rate | 0.4165 |
| sharpe_ratio | -10.2782 |
| sortino_ratio | -4.6627 |
| max_drawdown | 0.9973 |
| cagr | -0.9037 |
| net_avg_win | 15.7191 |
| net_avg_loss | -26.2768 |
| avg_hold_time_bars | 4.3631 |
| exposure | 0.2034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
