# EMA Hourly Continuation — CGPT/USDT P12_20

**Symbol:** CGPT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.7943 |
| net_win_rate | 0.5253 |
| gross_profit_factor | 1.0981 |
| gross_win_rate | 0.5253 |
| sharpe_ratio | -1.2213 |
| sortino_ratio | -0.3037 |
| max_drawdown | 0.3362 |
| cagr | -0.1301 |
| net_avg_win | 73.1113 |
| net_avg_loss | -101.8410 |
| avg_hold_time_bars | 5.2694 |
| exposure | 0.0711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
