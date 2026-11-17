# EMA Hourly Continuation — GMEE/USDT P20_50

**Symbol:** GMEE/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1004 |
| net_profit_factor | 0.4787 |
| net_win_rate | 0.4253 |
| gross_profit_factor | 0.7455 |
| gross_win_rate | 0.4343 |
| sharpe_ratio | -7.6590 |
| sortino_ratio | -3.4124 |
| max_drawdown | 0.9850 |
| cagr | -0.8117 |
| net_avg_win | 21.1772 |
| net_avg_loss | -32.7411 |
| avg_hold_time_bars | 4.9761 |
| exposure | 0.2271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
