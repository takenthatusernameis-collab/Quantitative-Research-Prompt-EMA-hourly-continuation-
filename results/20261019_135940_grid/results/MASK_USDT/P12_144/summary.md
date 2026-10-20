# EMA Hourly Continuation — MASK/USDT P12_144

**Symbol:** MASK/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.5038 |
| net_win_rate | 0.4376 |
| gross_profit_factor | 0.7782 |
| gross_win_rate | 0.4499 |
| sharpe_ratio | -4.8789 |
| sortino_ratio | -1.6351 |
| max_drawdown | 0.8676 |
| cagr | -0.5469 |
| net_avg_win | 35.1927 |
| net_avg_loss | -54.3532 |
| avg_hold_time_bars | 25.3796 |
| exposure | 0.6564 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
