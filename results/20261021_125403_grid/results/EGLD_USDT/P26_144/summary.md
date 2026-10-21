# EMA Hourly Continuation — EGLD/USDT P26_144

**Symbol:** EGLD/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7931 |
| net_win_rate | 0.5027 |
| gross_profit_factor | 0.9900 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -1.2768 |
| sortino_ratio | -0.3539 |
| max_drawdown | 0.3840 |
| cagr | -0.1515 |
| net_avg_win | 68.9252 |
| net_avg_loss | -87.8366 |
| avg_hold_time_bars | 28.2914 |
| exposure | 0.4810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
