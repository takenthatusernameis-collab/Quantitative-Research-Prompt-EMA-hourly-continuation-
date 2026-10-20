# EMA Hourly Continuation — LUNA/USDT P12_50

**Symbol:** LUNA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1250 |
| net_profit_factor | 0.4738 |
| net_win_rate | 0.4128 |
| gross_profit_factor | 0.8500 |
| gross_win_rate | 0.4256 |
| sharpe_ratio | -10.0261 |
| sortino_ratio | -5.0073 |
| max_drawdown | 0.9980 |
| cagr | -0.9153 |
| net_avg_win | 17.4135 |
| net_avg_loss | -25.8379 |
| avg_hold_time_bars | 5.6336 |
| exposure | 0.3201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
