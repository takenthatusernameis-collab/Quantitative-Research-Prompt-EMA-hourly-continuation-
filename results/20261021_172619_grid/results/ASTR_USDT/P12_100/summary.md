# EMA Hourly Continuation — ASTR/USDT P12_100

**Symbol:** ASTR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.7755 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 0.9923 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -1.8263 |
| sortino_ratio | -0.5738 |
| max_drawdown | 0.5182 |
| cagr | -0.2328 |
| net_avg_win | 70.1629 |
| net_avg_loss | -88.6278 |
| avg_hold_time_bars | 26.5670 |
| exposure | 0.5831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
