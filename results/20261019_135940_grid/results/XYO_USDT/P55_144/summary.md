# EMA Hourly Continuation — XYO/USDT P55_144

**Symbol:** XYO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.4230 |
| net_win_rate | 0.4003 |
| gross_profit_factor | 0.7135 |
| gross_win_rate | 0.4082 |
| sharpe_ratio | -7.0012 |
| sortino_ratio | -2.4788 |
| max_drawdown | 0.9561 |
| cagr | -0.7069 |
| net_avg_win | 27.6703 |
| net_avg_loss | -43.6633 |
| avg_hold_time_bars | 9.3687 |
| exposure | 0.2679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
