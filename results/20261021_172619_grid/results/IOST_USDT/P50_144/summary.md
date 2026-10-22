# EMA Hourly Continuation — IOST/USDT P50_144

**Symbol:** IOST/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.8019 |
| net_win_rate | 0.5225 |
| gross_profit_factor | 1.0838 |
| gross_win_rate | 0.5225 |
| sharpe_ratio | -1.3493 |
| sortino_ratio | -0.3884 |
| max_drawdown | 0.3917 |
| cagr | -0.1645 |
| net_avg_win | 70.3699 |
| net_avg_loss | -96.0211 |
| avg_hold_time_bars | 15.5425 |
| exposure | 0.2826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
