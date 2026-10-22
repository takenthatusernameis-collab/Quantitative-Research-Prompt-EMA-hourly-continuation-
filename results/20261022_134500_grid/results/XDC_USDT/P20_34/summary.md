# EMA Hourly Continuation — XDC/USDT P20_34

**Symbol:** XDC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1177 |
| net_profit_factor | 0.1133 |
| net_win_rate | 0.3364 |
| gross_profit_factor | 0.4263 |
| gross_win_rate | 0.4282 |
| sharpe_ratio | -15.2666 |
| sortino_ratio | -7.7029 |
| max_drawdown | 1.0000 |
| cagr | -0.9844 |
| net_avg_win | 3.2281 |
| net_avg_loss | -14.4405 |
| avg_hold_time_bars | 3.0076 |
| exposure | 0.1609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
