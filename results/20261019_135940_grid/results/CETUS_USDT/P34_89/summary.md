# EMA Hourly Continuation — CETUS/USDT P34_89

**Symbol:** CETUS/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.6728 |
| net_win_rate | 0.4842 |
| gross_profit_factor | 0.9852 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -3.5783 |
| sortino_ratio | -1.3350 |
| max_drawdown | 0.7992 |
| cagr | -0.4666 |
| net_avg_win | 48.5244 |
| net_avg_loss | -67.6983 |
| avg_hold_time_bars | 7.8563 |
| exposure | 0.2474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
