# EMA Hourly Continuation — DEGEN/USDT P21_144

**Symbol:** DEGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.9399 |
| net_win_rate | 0.5205 |
| gross_profit_factor | 1.0856 |
| gross_win_rate | 0.5205 |
| sharpe_ratio | -0.3998 |
| sortino_ratio | -0.1136 |
| max_drawdown | 0.3173 |
| cagr | -0.0564 |
| net_avg_win | 104.2745 |
| net_avg_loss | -120.4342 |
| avg_hold_time_bars | 29.5641 |
| exposure | 0.5249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
