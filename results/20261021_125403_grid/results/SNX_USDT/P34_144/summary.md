# EMA Hourly Continuation — SNX/USDT P34_144

**Symbol:** SNX/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.8151 |
| net_win_rate | 0.4974 |
| gross_profit_factor | 0.9967 |
| gross_win_rate | 0.4974 |
| sharpe_ratio | -1.2892 |
| sortino_ratio | -0.3580 |
| max_drawdown | 0.3660 |
| cagr | -0.1532 |
| net_avg_win | 80.3760 |
| net_avg_loss | -97.5658 |
| avg_hold_time_bars | 21.5847 |
| exposure | 0.3692 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
