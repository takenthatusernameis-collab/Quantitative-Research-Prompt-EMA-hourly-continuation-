# EMA Hourly Continuation — DCR/USDT P34_89

**Symbol:** DCR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.5980 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.8207 |
| gross_win_rate | 0.4492 |
| sharpe_ratio | -3.4637 |
| sortino_ratio | -1.0683 |
| max_drawdown | 0.7164 |
| cagr | -0.3880 |
| net_avg_win | 49.8483 |
| net_avg_loss | -67.9636 |
| avg_hold_time_bars | 10.3941 |
| exposure | 0.2220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
