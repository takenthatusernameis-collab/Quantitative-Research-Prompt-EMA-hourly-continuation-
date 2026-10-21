# EMA Hourly Continuation — CRO/USDT P8_55

**Symbol:** CRO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.6678 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 0.9295 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -3.2838 |
| sortino_ratio | -1.2399 |
| max_drawdown | 0.7699 |
| cagr | -0.4347 |
| net_avg_win | 45.1544 |
| net_avg_loss | -63.8450 |
| avg_hold_time_bars | 13.5917 |
| exposure | 0.4312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
