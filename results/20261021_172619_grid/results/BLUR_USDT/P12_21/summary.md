# EMA Hourly Continuation — BLUR/USDT P12_21

**Symbol:** BLUR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.5824 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.8242 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -3.6334 |
| sortino_ratio | -1.0640 |
| max_drawdown | 0.7099 |
| cagr | -0.3869 |
| net_avg_win | 52.3013 |
| net_avg_loss | -72.8495 |
| avg_hold_time_bars | 4.6185 |
| exposure | 0.0882 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
