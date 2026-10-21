# EMA Hourly Continuation — STRK/USDT P26_89

**Symbol:** STRK/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.8041 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 0.9940 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.5046 |
| sortino_ratio | -0.4647 |
| max_drawdown | 0.4739 |
| cagr | -0.1935 |
| net_avg_win | 73.8203 |
| net_avg_loss | -91.4133 |
| avg_hold_time_bars | 13.4710 |
| exposure | 0.2847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
