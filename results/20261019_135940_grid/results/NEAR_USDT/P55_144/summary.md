# EMA Hourly Continuation — NEAR/USDT P55_144

**Symbol:** NEAR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.6074 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.9079 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -3.3370 |
| sortino_ratio | -1.0272 |
| max_drawdown | 0.7182 |
| cagr | -0.3924 |
| net_avg_win | 48.2367 |
| net_avg_loss | -71.5930 |
| avg_hold_time_bars | 9.3395 |
| exposure | 0.2050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
