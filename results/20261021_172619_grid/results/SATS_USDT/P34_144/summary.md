# EMA Hourly Continuation — SATS/USDT P34_144

**Symbol:** SATS/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.6762 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.8328 |
| gross_win_rate | 0.4484 |
| sharpe_ratio | -2.5044 |
| sortino_ratio | -0.6791 |
| max_drawdown | 0.6002 |
| cagr | -0.2690 |
| net_avg_win | 69.5739 |
| net_avg_loss | -82.7127 |
| avg_hold_time_bars | 20.2554 |
| exposure | 0.3373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
