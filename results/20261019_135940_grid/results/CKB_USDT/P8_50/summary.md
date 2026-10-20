# EMA Hourly Continuation — CKB/USDT P8_50

**Symbol:** CKB/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1144 |
| net_profit_factor | 0.6157 |
| net_win_rate | 0.4423 |
| gross_profit_factor | 0.9280 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -6.9739 |
| sortino_ratio | -3.3233 |
| max_drawdown | 0.9819 |
| cagr | -0.7962 |
| net_avg_win | 31.0780 |
| net_avg_loss | -40.0333 |
| avg_hold_time_bars | 8.8348 |
| exposure | 0.4594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
