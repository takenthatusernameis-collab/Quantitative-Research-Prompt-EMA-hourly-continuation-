# EMA Hourly Continuation — ATOM/USDT P34_89

**Symbol:** ATOM/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.5577 |
| net_win_rate | 0.5062 |
| gross_profit_factor | 1.0208 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -4.1254 |
| sortino_ratio | -1.4735 |
| max_drawdown | 0.8418 |
| cagr | -0.5117 |
| net_avg_win | 32.2875 |
| net_avg_loss | -59.3489 |
| avg_hold_time_bars | 8.4301 |
| exposure | 0.2468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
