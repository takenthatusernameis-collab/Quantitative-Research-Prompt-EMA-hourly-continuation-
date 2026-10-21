# EMA Hourly Continuation — DUSK/USDT P26_200

**Symbol:** DUSK/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.8926 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 1.0162 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -0.5596 |
| sortino_ratio | -0.1312 |
| max_drawdown | 0.2162 |
| cagr | -0.0612 |
| net_avg_win | 90.2607 |
| net_avg_loss | -102.6469 |
| avg_hold_time_bars | 47.3097 |
| exposure | 0.5763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
