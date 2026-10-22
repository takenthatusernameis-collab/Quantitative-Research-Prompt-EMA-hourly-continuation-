# EMA Hourly Continuation — JASMY/USDT P26_100

**Symbol:** JASMY/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.6764 |
| net_win_rate | 0.5030 |
| gross_profit_factor | 1.0079 |
| gross_win_rate | 0.5118 |
| sharpe_ratio | -3.0188 |
| sortino_ratio | -1.1106 |
| max_drawdown | 0.7651 |
| cagr | -0.4091 |
| net_avg_win | 45.0651 |
| net_avg_loss | -67.4227 |
| avg_hold_time_bars | 10.5444 |
| exposure | 0.3240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
