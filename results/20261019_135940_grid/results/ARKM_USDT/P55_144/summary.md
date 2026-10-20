# EMA Hourly Continuation — ARKM/USDT P55_144

**Symbol:** ARKM/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.7221 |
| net_win_rate | 0.5047 |
| gross_profit_factor | 1.0337 |
| gross_win_rate | 0.5104 |
| sharpe_ratio | -2.3959 |
| sortino_ratio | -0.7730 |
| max_drawdown | 0.6151 |
| cagr | -0.3089 |
| net_avg_win | 59.0556 |
| net_avg_loss | -83.3530 |
| avg_hold_time_bars | 9.8956 |
| exposure | 0.2370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
