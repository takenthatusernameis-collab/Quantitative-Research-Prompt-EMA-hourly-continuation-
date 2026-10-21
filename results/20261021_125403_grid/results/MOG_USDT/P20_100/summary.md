# EMA Hourly Continuation — MOG/USDT P20_100

**Symbol:** MOG/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.8010 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9328 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -1.4786 |
| sortino_ratio | -0.4431 |
| max_drawdown | 0.4431 |
| cagr | -0.1855 |
| net_avg_win | 77.1704 |
| net_avg_loss | -90.7856 |
| avg_hold_time_bars | 20.1411 |
| exposure | 0.4045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
