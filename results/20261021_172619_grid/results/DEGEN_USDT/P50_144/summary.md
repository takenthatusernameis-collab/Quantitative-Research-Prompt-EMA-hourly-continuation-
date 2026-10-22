# EMA Hourly Continuation — DEGEN/USDT P50_144

**Symbol:** DEGEN/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.9365 |
| net_win_rate | 0.5271 |
| gross_profit_factor | 1.1122 |
| gross_win_rate | 0.5271 |
| sharpe_ratio | -0.3885 |
| sortino_ratio | -0.1050 |
| max_drawdown | 0.2897 |
| cagr | -0.0517 |
| net_avg_win | 99.3702 |
| net_avg_loss | -118.2554 |
| avg_hold_time_bars | 17.3818 |
| exposure | 0.2778 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
