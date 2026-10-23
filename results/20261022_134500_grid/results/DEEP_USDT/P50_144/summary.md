# EMA Hourly Continuation — DEEP/USDT P50_144

**Symbol:** DEEP/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.7318 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0090 |
| gross_win_rate | 0.5100 |
| sharpe_ratio | -1.8856 |
| sortino_ratio | -0.5584 |
| max_drawdown | 0.4204 |
| cagr | -0.2316 |
| net_avg_win | 63.8798 |
| net_avg_loss | -88.8058 |
| avg_hold_time_bars | 16.0000 |
| exposure | 0.3162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
