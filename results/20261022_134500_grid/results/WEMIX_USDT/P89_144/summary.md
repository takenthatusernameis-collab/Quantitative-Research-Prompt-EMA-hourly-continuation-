# EMA Hourly Continuation — WEMIX/USDT P89_144

**Symbol:** WEMIX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 808 |
| net_profit_factor | 0.2469 |
| net_win_rate | 0.2871 |
| gross_profit_factor | 0.4411 |
| gross_win_rate | 0.2995 |
| sharpe_ratio | -12.5113 |
| sortino_ratio | -5.1342 |
| max_drawdown | 0.9987 |
| cagr | -0.9293 |
| net_avg_win | 14.1118 |
| net_avg_loss | -23.0226 |
| avg_hold_time_bars | 4.5210 |
| exposure | 0.1660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
