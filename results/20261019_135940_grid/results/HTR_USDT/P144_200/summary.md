# EMA Hourly Continuation — HTR/USDT P144_200

**Symbol:** HTR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.3962 |
| net_win_rate | 0.4046 |
| gross_profit_factor | 0.6943 |
| gross_win_rate | 0.4170 |
| sharpe_ratio | -6.4296 |
| sortino_ratio | -1.9568 |
| max_drawdown | 0.9289 |
| cagr | -0.6452 |
| net_avg_win | 31.1541 |
| net_avg_loss | -53.4291 |
| avg_hold_time_bars | 4.8900 |
| exposure | 0.1071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
