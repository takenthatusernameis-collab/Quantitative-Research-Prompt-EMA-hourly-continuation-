# EMA Hourly Continuation — CYBER/USDT P8_200

**Symbol:** CYBER/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 231 |
| net_profit_factor | 0.8317 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9751 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -0.8760 |
| sortino_ratio | -0.1902 |
| max_drawdown | 0.3162 |
| cagr | -0.0849 |
| net_avg_win | 86.6184 |
| net_avg_loss | -101.4742 |
| avg_hold_time_bars | 80.8052 |
| exposure | 0.8485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
