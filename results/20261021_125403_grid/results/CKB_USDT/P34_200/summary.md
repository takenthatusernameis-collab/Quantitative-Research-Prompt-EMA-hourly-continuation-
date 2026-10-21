# EMA Hourly Continuation — CKB/USDT P34_200

**Symbol:** CKB/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.7469 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9223 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -1.6201 |
| sortino_ratio | -0.4139 |
| max_drawdown | 0.3875 |
| cagr | -0.1741 |
| net_avg_win | 72.6102 |
| net_avg_loss | -90.7792 |
| avg_hold_time_bars | 34.1495 |
| exposure | 0.4983 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
