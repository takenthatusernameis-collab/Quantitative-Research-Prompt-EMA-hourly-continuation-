# EMA Hourly Continuation — XCN/USDT P12_50

**Symbol:** XCN/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1275 |
| net_profit_factor | 0.3615 |
| net_win_rate | 0.3914 |
| gross_profit_factor | 0.6374 |
| gross_win_rate | 0.4118 |
| sharpe_ratio | -10.7874 |
| sortino_ratio | -5.4078 |
| max_drawdown | 0.9990 |
| cagr | -0.9360 |
| net_avg_win | 11.3360 |
| net_avg_loss | -20.1632 |
| avg_hold_time_bars | 6.1898 |
| exposure | 0.3587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
