# EMA Hourly Continuation — PENDLE/USDT P8_20

**Symbol:** PENDLE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.6420 |
| net_win_rate | 0.4538 |
| gross_profit_factor | 0.8389 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -3.2657 |
| sortino_ratio | -1.0598 |
| max_drawdown | 0.7100 |
| cagr | -0.3846 |
| net_avg_win | 53.5251 |
| net_avg_loss | -69.2861 |
| avg_hold_time_bars | 5.9615 |
| exposure | 0.1409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
