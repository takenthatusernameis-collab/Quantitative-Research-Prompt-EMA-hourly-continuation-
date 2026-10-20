# EMA Hourly Continuation — ETN/USDT P12_89

**Symbol:** ETN/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 795 |
| net_profit_factor | 0.3615 |
| net_win_rate | 0.3547 |
| gross_profit_factor | 0.5303 |
| gross_win_rate | 0.3723 |
| sharpe_ratio | -9.3560 |
| sortino_ratio | -4.0737 |
| max_drawdown | 0.9837 |
| cagr | -0.8586 |
| net_avg_win | 19.7482 |
| net_avg_loss | -30.0295 |
| avg_hold_time_bars | 10.3660 |
| exposure | 0.4476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
