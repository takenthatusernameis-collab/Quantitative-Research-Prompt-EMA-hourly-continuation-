# EMA Hourly Continuation — CKB/USDT P12_34

**Symbol:** CKB/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.6917 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.9193 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -3.5544 |
| sortino_ratio | -1.3005 |
| max_drawdown | 0.7863 |
| cagr | -0.4485 |
| net_avg_win | 56.6756 |
| net_avg_loss | -71.8751 |
| avg_hold_time_bars | 6.5890 |
| exposure | 0.1968 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
