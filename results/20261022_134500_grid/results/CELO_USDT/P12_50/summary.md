# EMA Hourly Continuation — CELO/USDT P12_50

**Symbol:** CELO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1015 |
| net_profit_factor | 0.5763 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.9328 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -5.8317 |
| sortino_ratio | -2.6201 |
| max_drawdown | 0.9578 |
| cagr | -0.7112 |
| net_avg_win | 27.6756 |
| net_avg_loss | -41.4157 |
| avg_hold_time_bars | 8.1921 |
| exposure | 0.3763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
