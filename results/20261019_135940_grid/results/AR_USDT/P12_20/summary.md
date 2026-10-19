# EMA Hourly Continuation — AR/USDT P12_20

**Symbol:** AR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1561 |
| net_profit_factor | 0.3193 |
| net_win_rate | 0.3965 |
| gross_profit_factor | 0.6942 |
| gross_win_rate | 0.4247 |
| sharpe_ratio | -13.3734 |
| sortino_ratio | -7.4747 |
| max_drawdown | 0.9999 |
| cagr | -0.9787 |
| net_avg_win | 7.5766 |
| net_avg_loss | -15.5937 |
| avg_hold_time_bars | 2.1307 |
| exposure | 0.1512 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
