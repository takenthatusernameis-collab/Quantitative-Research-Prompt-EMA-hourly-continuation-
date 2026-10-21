# EMA Hourly Continuation — TURBO/USDT P89_200

**Symbol:** TURBO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.6689 |
| net_win_rate | 0.4927 |
| gross_profit_factor | 0.9404 |
| gross_win_rate | 0.4927 |
| sharpe_ratio | -2.4782 |
| sortino_ratio | -0.7073 |
| max_drawdown | 0.5206 |
| cagr | -0.2872 |
| net_avg_win | 60.6709 |
| net_avg_loss | -88.0945 |
| avg_hold_time_bars | 10.6997 |
| exposure | 0.2002 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
