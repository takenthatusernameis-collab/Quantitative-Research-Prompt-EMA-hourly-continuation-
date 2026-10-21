# EMA Hourly Continuation — AGLD/USDT P12_21

**Symbol:** AGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 604 |
| net_profit_factor | 0.6010 |
| net_win_rate | 0.4669 |
| gross_profit_factor | 0.8841 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -3.9796 |
| sortino_ratio | -1.3965 |
| max_drawdown | 0.8077 |
| cagr | -0.4727 |
| net_avg_win | 42.7847 |
| net_avg_loss | -62.3439 |
| avg_hold_time_bars | 5.0762 |
| exposure | 0.1388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
