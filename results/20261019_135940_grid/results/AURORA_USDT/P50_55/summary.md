# EMA Hourly Continuation — AURORA/USDT P50_55

**Symbol:** AURORA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 708 |
| net_profit_factor | 0.1876 |
| net_win_rate | 0.3065 |
| gross_profit_factor | 0.6578 |
| gross_win_rate | 0.3785 |
| sharpe_ratio | -12.9023 |
| sortino_ratio | -5.1756 |
| max_drawdown | 0.9992 |
| cagr | -0.9422 |
| net_avg_win | 10.6350 |
| net_avg_loss | -25.0510 |
| avg_hold_time_bars | 2.7881 |
| exposure | 0.0897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
