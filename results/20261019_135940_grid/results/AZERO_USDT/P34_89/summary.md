# EMA Hourly Continuation — AZERO/USDT P34_89

**Symbol:** AZERO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.5313 |
| net_win_rate | 0.4467 |
| gross_profit_factor | 0.8543 |
| gross_win_rate | 0.4552 |
| sharpe_ratio | -4.6964 |
| sortino_ratio | -1.5960 |
| max_drawdown | 0.8651 |
| cagr | -0.5395 |
| net_avg_win | 36.8658 |
| net_avg_loss | -56.0193 |
| avg_hold_time_bars | 10.0728 |
| exposure | 0.2694 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
