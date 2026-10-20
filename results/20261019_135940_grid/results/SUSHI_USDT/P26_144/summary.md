# EMA Hourly Continuation — SUSHI/USDT P26_144

**Symbol:** SUSHI/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.5763 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.8329 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -3.9871 |
| sortino_ratio | -1.2769 |
| max_drawdown | 0.7922 |
| cagr | -0.4581 |
| net_avg_win | 46.1389 |
| net_avg_loss | -64.4885 |
| avg_hold_time_bars | 20.4327 |
| exposure | 0.4808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
