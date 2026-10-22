# EMA Hourly Continuation — CPOOL/USDT P12_20

**Symbol:** CPOOL/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.8172 |
| net_win_rate | 0.5070 |
| gross_profit_factor | 1.0442 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -1.1817 |
| sortino_ratio | -0.2867 |
| max_drawdown | 0.3696 |
| cagr | -0.1248 |
| net_avg_win | 87.7259 |
| net_avg_loss | -110.3893 |
| avg_hold_time_bars | 5.3916 |
| exposure | 0.0701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
