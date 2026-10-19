# EMA Hourly Continuation — FET/USDT P100_144

**Symbol:** FET/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.5782 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 0.9802 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -3.6676 |
| sortino_ratio | -1.1004 |
| max_drawdown | 0.7437 |
| cagr | -0.4135 |
| net_avg_win | 45.3825 |
| net_avg_loss | -75.4396 |
| avg_hold_time_bars | 4.4703 |
| exposure | 0.0925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
