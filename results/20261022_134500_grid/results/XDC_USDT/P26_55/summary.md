# EMA Hourly Continuation — XDC/USDT P26_55

**Symbol:** XDC/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1018 |
| net_profit_factor | 0.1761 |
| net_win_rate | 0.3880 |
| gross_profit_factor | 0.5468 |
| gross_win_rate | 0.4371 |
| sharpe_ratio | -11.9174 |
| sortino_ratio | -5.4334 |
| max_drawdown | 0.9993 |
| cagr | -0.9450 |
| net_avg_win | 5.4090 |
| net_avg_loss | -19.4698 |
| avg_hold_time_bars | 4.1198 |
| exposure | 0.1906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
