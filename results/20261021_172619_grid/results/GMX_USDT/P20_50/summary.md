# EMA Hourly Continuation — GMX/USDT P20_50

**Symbol:** GMX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.6683 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.9275 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -3.3748 |
| sortino_ratio | -1.1926 |
| max_drawdown | 0.7583 |
| cagr | -0.4212 |
| net_avg_win | 51.6905 |
| net_avg_loss | -70.1204 |
| avg_hold_time_bars | 7.3856 |
| exposure | 0.2055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
