# EMA Hourly Continuation — ILV/USDT P26_34

**Symbol:** ILV/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 226 |
| net_profit_factor | 0.6482 |
| net_win_rate | 0.4956 |
| gross_profit_factor | 0.9538 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -1.8809 |
| sortino_ratio | -0.4065 |
| max_drawdown | 0.3891 |
| cagr | -0.1676 |
| net_avg_win | 60.7398 |
| net_avg_loss | -92.0619 |
| avg_hold_time_bars | 5.1593 |
| exposure | 0.0530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
