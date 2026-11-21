# EMA Hourly Continuation — HTR/USDT P12_55

**Symbol:** HTR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1046 |
| net_profit_factor | 0.4642 |
| net_win_rate | 0.3929 |
| gross_profit_factor | 0.7033 |
| gross_win_rate | 0.4015 |
| sharpe_ratio | -8.5827 |
| sortino_ratio | -3.9014 |
| max_drawdown | 0.9919 |
| cagr | -0.8511 |
| net_avg_win | 20.9070 |
| net_avg_loss | -29.1481 |
| avg_hold_time_bars | 7.3136 |
| exposure | 0.3477 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
