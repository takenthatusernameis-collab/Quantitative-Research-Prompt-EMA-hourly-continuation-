# EMA Hourly Continuation — BIGTIME/USDT P26_100

**Symbol:** BIGTIME/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.8600 |
| net_win_rate | 0.5174 |
| gross_profit_factor | 1.0722 |
| gross_win_rate | 0.5174 |
| sharpe_ratio | -1.0486 |
| sortino_ratio | -0.3223 |
| max_drawdown | 0.4197 |
| cagr | -0.1405 |
| net_avg_win | 81.8908 |
| net_avg_loss | -102.0887 |
| avg_hold_time_bars | 18.0283 |
| exposure | 0.3753 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
