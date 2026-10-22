# EMA Hourly Continuation — TRADE/USDT P8_12

**Symbol:** TRADE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1557 |
| net_profit_factor | 0.2673 |
| net_win_rate | 0.3096 |
| gross_profit_factor | 0.7182 |
| gross_win_rate | 0.3359 |
| sharpe_ratio | -18.5182 |
| sortino_ratio | -10.6763 |
| max_drawdown | 1.0000 |
| cagr | -0.9972 |
| net_avg_win | 7.5675 |
| net_avg_loss | -12.6954 |
| avg_hold_time_bars | 2.5556 |
| exposure | 0.1809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
