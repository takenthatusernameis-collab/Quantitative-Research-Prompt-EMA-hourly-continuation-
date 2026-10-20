# EMA Hourly Continuation — MAGIC/USDT P50_144

**Symbol:** MAGIC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.5944 |
| net_win_rate | 0.4566 |
| gross_profit_factor | 0.8884 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -3.4909 |
| sortino_ratio | -1.0457 |
| max_drawdown | 0.7238 |
| cagr | -0.3903 |
| net_avg_win | 50.8539 |
| net_avg_loss | -71.8798 |
| avg_hold_time_bars | 15.1626 |
| exposure | 0.3095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
