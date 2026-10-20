# EMA Hourly Continuation — GMX/USDT P50_200

**Symbol:** GMX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.6449 |
| net_win_rate | 0.4537 |
| gross_profit_factor | 0.8798 |
| gross_win_rate | 0.4561 |
| sharpe_ratio | -3.1752 |
| sortino_ratio | -0.9161 |
| max_drawdown | 0.6972 |
| cagr | -0.3536 |
| net_avg_win | 63.2956 |
| net_avg_loss | -81.5054 |
| avg_hold_time_bars | 19.3515 |
| exposure | 0.3703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
