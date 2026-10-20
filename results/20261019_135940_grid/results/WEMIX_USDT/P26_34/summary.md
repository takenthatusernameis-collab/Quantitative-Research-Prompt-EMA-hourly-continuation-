# EMA Hourly Continuation — WEMIX/USDT P26_34

**Symbol:** WEMIX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1555 |
| net_profit_factor | 0.0930 |
| net_win_rate | 0.2238 |
| gross_profit_factor | 0.3094 |
| gross_win_rate | 0.2662 |
| sharpe_ratio | -22.5605 |
| sortino_ratio | -13.5236 |
| max_drawdown | 1.0000 |
| cagr | -0.9994 |
| net_avg_win | 2.9457 |
| net_avg_loss | -9.1343 |
| avg_hold_time_bars | 2.3164 |
| exposure | 0.1637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
