# EMA Hourly Continuation — BOSON/USDT P12_34

**Symbol:** BOSON/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1089 |
| net_profit_factor | 0.5144 |
| net_win_rate | 0.4417 |
| gross_profit_factor | 0.8585 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -6.8904 |
| sortino_ratio | -3.1873 |
| max_drawdown | 0.9793 |
| cagr | -0.7851 |
| net_avg_win | 21.5572 |
| net_avg_loss | -33.1556 |
| avg_hold_time_bars | 5.2911 |
| exposure | 0.2619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
