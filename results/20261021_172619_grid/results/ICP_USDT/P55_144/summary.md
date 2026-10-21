# EMA Hourly Continuation — ICP/USDT P55_144

**Symbol:** ICP/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.7917 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0047 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.3565 |
| sortino_ratio | -0.3464 |
| max_drawdown | 0.4072 |
| cagr | -0.1476 |
| net_avg_win | 78.9612 |
| net_avg_loss | -99.7345 |
| avg_hold_time_bars | 16.1509 |
| exposure | 0.2335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
