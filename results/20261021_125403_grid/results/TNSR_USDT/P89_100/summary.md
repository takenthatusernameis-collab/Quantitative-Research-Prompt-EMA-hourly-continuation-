# EMA Hourly Continuation — TNSR/USDT P89_100

**Symbol:** TNSR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 156 |
| net_profit_factor | 0.5366 |
| net_win_rate | 0.4487 |
| gross_profit_factor | 0.8093 |
| gross_win_rate | 0.4487 |
| sharpe_ratio | -2.4210 |
| sortino_ratio | -0.4265 |
| max_drawdown | 0.4049 |
| cagr | -0.1846 |
| net_avg_win | 66.5513 |
| net_avg_loss | -100.9536 |
| avg_hold_time_bars | 4.6154 |
| exposure | 0.0326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
