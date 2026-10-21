# EMA Hourly Continuation — GMT/USDT P12_26

**Symbol:** GMT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.7026 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 0.9851 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -2.2003 |
| sortino_ratio | -0.6800 |
| max_drawdown | 0.5583 |
| cagr | -0.2673 |
| net_avg_win | 55.1976 |
| net_avg_loss | -79.2464 |
| avg_hold_time_bars | 5.3506 |
| exposure | 0.1124 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
