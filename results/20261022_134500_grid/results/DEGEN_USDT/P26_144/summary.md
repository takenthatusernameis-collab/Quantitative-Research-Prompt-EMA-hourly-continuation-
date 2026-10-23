# EMA Hourly Continuation — DEGEN/USDT P26_144

**Symbol:** DEGEN/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.7241 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.9356 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -2.5391 |
| sortino_ratio | -0.7805 |
| max_drawdown | 0.6172 |
| cagr | -0.3085 |
| net_avg_win | 70.7135 |
| net_avg_loss | -87.4982 |
| avg_hold_time_bars | 22.0422 |
| exposure | 0.4757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
