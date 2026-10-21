# EMA Hourly Continuation — ZETA/USDT P26_144

**Symbol:** ZETA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.8959 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0759 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -0.6452 |
| sortino_ratio | -0.1688 |
| max_drawdown | 0.3268 |
| cagr | -0.0780 |
| net_avg_win | 92.6095 |
| net_avg_loss | -110.4356 |
| avg_hold_time_bars | 34.6667 |
| exposure | 0.5224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
