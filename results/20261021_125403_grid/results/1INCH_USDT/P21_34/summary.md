# EMA Hourly Continuation — 1INCH/USDT P21_34

**Symbol:** 1INCH/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.5110 |
| net_win_rate | 0.4438 |
| gross_profit_factor | 0.7783 |
| gross_win_rate | 0.4438 |
| sharpe_ratio | -3.8063 |
| sortino_ratio | -1.0153 |
| max_drawdown | 0.6911 |
| cagr | -0.3736 |
| net_avg_win | 46.8889 |
| net_avg_loss | -73.2224 |
| avg_hold_time_bars | 4.6801 |
| exposure | 0.0738 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
