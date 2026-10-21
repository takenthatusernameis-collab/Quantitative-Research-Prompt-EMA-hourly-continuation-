# EMA Hourly Continuation — CKB/USDT P12_55

**Symbol:** CKB/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.7031 |
| net_win_rate | 0.4666 |
| gross_profit_factor | 0.8949 |
| gross_win_rate | 0.4666 |
| sharpe_ratio | -3.2823 |
| sortino_ratio | -1.2257 |
| max_drawdown | 0.7696 |
| cagr | -0.4305 |
| net_avg_win | 55.8309 |
| net_avg_loss | -69.4538 |
| avg_hold_time_bars | 10.7907 |
| exposure | 0.3375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
