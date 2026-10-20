# EMA Hourly Continuation — W/USDT P12_34

**Symbol:** W/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1287 |
| net_profit_factor | 0.5934 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.9865 |
| gross_win_rate | 0.4911 |
| sharpe_ratio | -6.4271 |
| sortino_ratio | -3.2552 |
| max_drawdown | 0.9815 |
| cagr | -0.7907 |
| net_avg_win | 23.3360 |
| net_avg_loss | -35.7688 |
| avg_hold_time_bars | 4.1422 |
| exposure | 0.2423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
