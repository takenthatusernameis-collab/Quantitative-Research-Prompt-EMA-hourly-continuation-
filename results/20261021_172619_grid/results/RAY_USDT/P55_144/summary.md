# EMA Hourly Continuation — RAY/USDT P55_144

**Symbol:** RAY/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.7343 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9033 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -1.6533 |
| sortino_ratio | -0.4294 |
| max_drawdown | 0.4618 |
| cagr | -0.1802 |
| net_avg_win | 67.8570 |
| net_avg_loss | -85.9631 |
| avg_hold_time_bars | 15.4127 |
| exposure | 0.2326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
