# EMA Hourly Continuation — SUPER/USDT P55_200

**Symbol:** SUPER/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.8843 |
| net_win_rate | 0.5236 |
| gross_profit_factor | 1.0821 |
| gross_win_rate | 0.5236 |
| sharpe_ratio | -0.6025 |
| sortino_ratio | -0.1490 |
| max_drawdown | 0.2437 |
| cagr | -0.0689 |
| net_avg_win | 80.9328 |
| net_avg_loss | -100.6079 |
| avg_hold_time_bars | 25.6182 |
| exposure | 0.3447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
