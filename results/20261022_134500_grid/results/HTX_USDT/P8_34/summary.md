# EMA Hourly Continuation — HTX/USDT P8_34

**Symbol:** HTX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1446 |
| net_profit_factor | 0.1700 |
| net_win_rate | 0.2801 |
| gross_profit_factor | 0.5533 |
| gross_win_rate | 0.3589 |
| sharpe_ratio | -19.2013 |
| sortino_ratio | -10.9045 |
| max_drawdown | 1.0000 |
| cagr | -0.9974 |
| net_avg_win | 5.0584 |
| net_avg_loss | -11.5741 |
| avg_hold_time_bars | 5.8451 |
| exposure | 0.3825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
