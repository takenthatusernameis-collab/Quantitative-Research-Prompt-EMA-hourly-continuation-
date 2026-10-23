# EMA Hourly Continuation — AURORA/USDT P12_50

**Symbol:** AURORA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 912 |
| net_profit_factor | 0.4808 |
| net_win_rate | 0.4145 |
| gross_profit_factor | 0.8659 |
| gross_win_rate | 0.4287 |
| sharpe_ratio | -8.3067 |
| sortino_ratio | -3.5058 |
| max_drawdown | 0.9894 |
| cagr | -0.8320 |
| net_avg_win | 24.2213 |
| net_avg_loss | -35.6596 |
| avg_hold_time_bars | 8.3980 |
| exposure | 0.3481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
