# EMA Hourly Continuation — AAVE/USDT P20_26

**Symbol:** AAVE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1209 |
| net_profit_factor | 0.1894 |
| net_win_rate | 0.3557 |
| gross_profit_factor | 0.5848 |
| gross_win_rate | 0.3896 |
| sharpe_ratio | -14.9439 |
| sortino_ratio | -7.5864 |
| max_drawdown | 1.0000 |
| cagr | -0.9840 |
| net_avg_win | 5.4349 |
| net_avg_loss | -15.8366 |
| avg_hold_time_bars | 1.9793 |
| exposure | 0.1088 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
