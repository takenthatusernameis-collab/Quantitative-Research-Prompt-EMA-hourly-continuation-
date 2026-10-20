# EMA Hourly Continuation — 1INCH/USDT P20_50

**Symbol:** 1INCH/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1059 |
| net_profit_factor | 0.4304 |
| net_win_rate | 0.4127 |
| gross_profit_factor | 0.7834 |
| gross_win_rate | 0.4400 |
| sharpe_ratio | -8.9802 |
| sortino_ratio | -4.1514 |
| max_drawdown | 0.9937 |
| cagr | -0.8670 |
| net_avg_win | 17.1798 |
| net_avg_loss | -28.0457 |
| avg_hold_time_bars | 4.7252 |
| exposure | 0.2275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
