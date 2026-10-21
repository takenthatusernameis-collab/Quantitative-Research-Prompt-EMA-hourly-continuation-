# EMA Hourly Continuation — FIL/USDT P12_144

**Symbol:** FIL/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.8105 |
| net_win_rate | 0.4968 |
| gross_profit_factor | 0.9748 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -1.1223 |
| sortino_ratio | -0.2841 |
| max_drawdown | 0.3362 |
| cagr | -0.1236 |
| net_avg_win | 77.3311 |
| net_avg_loss | -94.2006 |
| avg_hold_time_bars | 49.4713 |
| exposure | 0.7061 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
