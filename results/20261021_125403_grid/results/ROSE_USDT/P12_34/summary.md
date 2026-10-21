# EMA Hourly Continuation — ROSE/USDT P12_34

**Symbol:** ROSE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.7014 |
| net_win_rate | 0.4836 |
| gross_profit_factor | 0.9205 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -2.6906 |
| sortino_ratio | -0.9739 |
| max_drawdown | 0.6752 |
| cagr | -0.3596 |
| net_avg_win | 51.0341 |
| net_avg_loss | -68.1429 |
| avg_hold_time_bars | 6.3931 |
| exposure | 0.1863 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
