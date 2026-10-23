# EMA Hourly Continuation — BOSON/USDT P21_34

**Symbol:** BOSON/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 984 |
| net_profit_factor | 0.4618 |
| net_win_rate | 0.4390 |
| gross_profit_factor | 0.8976 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -7.6452 |
| sortino_ratio | -3.3710 |
| max_drawdown | 0.9848 |
| cagr | -0.8101 |
| net_avg_win | 19.5571 |
| net_avg_loss | -33.1419 |
| avg_hold_time_bars | 3.7022 |
| exposure | 0.1656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
