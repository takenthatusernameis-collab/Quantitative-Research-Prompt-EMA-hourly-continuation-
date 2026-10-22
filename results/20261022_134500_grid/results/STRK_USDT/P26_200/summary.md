# EMA Hourly Continuation — STRK/USDT P26_200

**Symbol:** STRK/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.6897 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.9271 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -2.4550 |
| sortino_ratio | -0.6943 |
| max_drawdown | 0.6022 |
| cagr | -0.2802 |
| net_avg_win | 65.3995 |
| net_avg_loss | -86.2477 |
| avg_hold_time_bars | 30.8354 |
| exposure | 0.5620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
