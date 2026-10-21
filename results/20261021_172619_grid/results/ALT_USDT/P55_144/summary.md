# EMA Hourly Continuation — ALT/USDT P55_144

**Symbol:** ALT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.6800 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8540 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -2.1790 |
| sortino_ratio | -0.5826 |
| max_drawdown | 0.4989 |
| cagr | -0.2354 |
| net_avg_win | 63.1512 |
| net_avg_loss | -81.0758 |
| avg_hold_time_bars | 17.5650 |
| exposure | 0.2826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
