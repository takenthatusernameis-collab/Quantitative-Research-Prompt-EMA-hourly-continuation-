# EMA Hourly Continuation — APE/USDT P26_200

**Symbol:** APE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.6634 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.9097 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -2.1369 |
| sortino_ratio | -0.5619 |
| max_drawdown | 0.5020 |
| cagr | -0.2310 |
| net_avg_win | 57.6913 |
| net_avg_loss | -80.1587 |
| avg_hold_time_bars | 38.1831 |
| exposure | 0.5970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
