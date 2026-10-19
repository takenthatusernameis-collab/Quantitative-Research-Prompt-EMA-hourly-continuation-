# EMA Hourly Continuation — FLOKI/USDT P50_144

**Symbol:** FLOKI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.6272 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.9049 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -3.1913 |
| sortino_ratio | -0.9964 |
| max_drawdown | 0.7005 |
| cagr | -0.3754 |
| net_avg_win | 50.7177 |
| net_avg_loss | -72.0865 |
| avg_hold_time_bars | 14.1230 |
| exposure | 0.3133 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
