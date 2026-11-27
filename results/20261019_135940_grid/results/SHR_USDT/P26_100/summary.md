# EMA Hourly Continuation — SHR/USDT P26_100

**Symbol:** SHR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 971 |
| net_profit_factor | 0.3885 |
| net_win_rate | 0.3347 |
| gross_profit_factor | 0.5622 |
| gross_win_rate | 0.3368 |
| sharpe_ratio | -9.3584 |
| sortino_ratio | -4.0725 |
| max_drawdown | 0.9931 |
| cagr | -0.8598 |
| net_avg_win | 19.4115 |
| net_avg_loss | -25.1368 |
| avg_hold_time_bars | 7.0402 |
| exposure | 0.3093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
