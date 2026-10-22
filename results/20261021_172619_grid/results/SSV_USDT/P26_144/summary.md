# EMA Hourly Continuation — SSV/USDT P26_144

**Symbol:** SSV/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.7830 |
| net_win_rate | 0.4865 |
| gross_profit_factor | 0.9500 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -1.4829 |
| sortino_ratio | -0.4059 |
| max_drawdown | 0.3989 |
| cagr | -0.1713 |
| net_avg_win | 75.6963 |
| net_avg_loss | -91.5809 |
| avg_hold_time_bars | 29.9081 |
| exposure | 0.5007 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
