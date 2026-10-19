# EMA Hourly Continuation — BTT/USDT P8_55

**Symbol:** BTT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 926 |
| net_profit_factor | 0.3435 |
| net_win_rate | 0.3801 |
| gross_profit_factor | 0.7441 |
| gross_win_rate | 0.4266 |
| sharpe_ratio | -10.7691 |
| sortino_ratio | -4.6447 |
| max_drawdown | 0.9980 |
| cagr | -0.9157 |
| net_avg_win | 14.8345 |
| net_avg_loss | -26.4837 |
| avg_hold_time_bars | 13.5724 |
| exposure | 0.5713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
