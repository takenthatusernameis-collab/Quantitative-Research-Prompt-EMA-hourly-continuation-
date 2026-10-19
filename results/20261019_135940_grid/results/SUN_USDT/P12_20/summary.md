# EMA Hourly Continuation — SUN/USDT P12_20

**Symbol:** SUN/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1327 |
| net_profit_factor | 0.0894 |
| net_win_rate | 0.2999 |
| gross_profit_factor | 0.5505 |
| gross_win_rate | 0.4250 |
| sharpe_ratio | -18.3856 |
| sortino_ratio | -10.1459 |
| max_drawdown | 1.0000 |
| cagr | -0.9963 |
| net_avg_win | 2.4662 |
| net_avg_loss | -11.8208 |
| avg_hold_time_bars | 3.2622 |
| exposure | 0.1959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
