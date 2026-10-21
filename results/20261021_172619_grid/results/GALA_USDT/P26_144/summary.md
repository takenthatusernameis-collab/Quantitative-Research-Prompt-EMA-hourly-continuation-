# EMA Hourly Continuation — GALA/USDT P26_144

**Symbol:** GALA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.8701 |
| net_win_rate | 0.5118 |
| gross_profit_factor | 1.0352 |
| gross_win_rate | 0.5118 |
| sharpe_ratio | -0.7045 |
| sortino_ratio | -0.1866 |
| max_drawdown | 0.2445 |
| cagr | -0.0849 |
| net_avg_win | 76.9140 |
| net_avg_loss | -92.6585 |
| avg_hold_time_bars | 31.0824 |
| exposure | 0.4804 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
