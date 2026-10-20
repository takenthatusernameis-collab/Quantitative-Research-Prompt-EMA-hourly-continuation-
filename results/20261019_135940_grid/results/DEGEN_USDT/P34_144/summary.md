# EMA Hourly Continuation — DEGEN/USDT P34_144

**Symbol:** DEGEN/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.7902 |
| net_win_rate | 0.4947 |
| gross_profit_factor | 1.0116 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -1.8914 |
| sortino_ratio | -0.5821 |
| max_drawdown | 0.5466 |
| cagr | -0.2392 |
| net_avg_win | 80.5478 |
| net_avg_loss | -99.7799 |
| avg_hold_time_bars | 19.3817 |
| exposure | 0.4139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
