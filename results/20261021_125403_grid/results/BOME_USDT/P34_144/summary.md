# EMA Hourly Continuation — BOME/USDT P34_144

**Symbol:** BOME/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.8767 |
| net_win_rate | 0.5124 |
| gross_profit_factor | 1.0246 |
| gross_win_rate | 0.5124 |
| sharpe_ratio | -0.6412 |
| sortino_ratio | -0.1754 |
| max_drawdown | 0.3172 |
| cagr | -0.0810 |
| net_avg_win | 73.0707 |
| net_avg_loss | -87.5847 |
| avg_hold_time_bars | 24.2755 |
| exposure | 0.4005 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
