# EMA Hourly Continuation — FLUX/USDT P12_144

**Symbol:** FLUX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.8141 |
| net_win_rate | 0.4975 |
| gross_profit_factor | 0.9744 |
| gross_win_rate | 0.4975 |
| sharpe_ratio | -1.1791 |
| sortino_ratio | -0.3381 |
| max_drawdown | 0.3673 |
| cagr | -0.1461 |
| net_avg_win | 71.6788 |
| net_avg_loss | -87.1742 |
| avg_hold_time_bars | 36.1816 |
| exposure | 0.6611 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
