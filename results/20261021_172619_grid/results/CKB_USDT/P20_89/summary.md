# EMA Hourly Continuation — CKB/USDT P20_89

**Symbol:** CKB/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.7825 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 0.9895 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -1.7736 |
| sortino_ratio | -0.5751 |
| max_drawdown | 0.4865 |
| cagr | -0.2331 |
| net_avg_win | 68.3812 |
| net_avg_loss | -87.0463 |
| avg_hold_time_bars | 15.2885 |
| exposure | 0.3565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
