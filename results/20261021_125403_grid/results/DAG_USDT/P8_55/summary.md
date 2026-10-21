# EMA Hourly Continuation — DAG/USDT P8_55

**Symbol:** DAG/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.8223 |
| net_win_rate | 0.4991 |
| gross_profit_factor | 0.9722 |
| gross_win_rate | 0.4991 |
| sharpe_ratio | -1.2996 |
| sortino_ratio | -0.4326 |
| max_drawdown | 0.4795 |
| cagr | -0.1827 |
| net_avg_win | 68.1303 |
| net_avg_loss | -82.5459 |
| avg_hold_time_bars | 17.0721 |
| exposure | 0.4198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
