# EMA Hourly Continuation — MOVR/USDT P34_89

**Symbol:** MOVR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 733 |
| net_profit_factor | 0.4868 |
| net_win_rate | 0.4393 |
| gross_profit_factor | 0.8142 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -5.7426 |
| sortino_ratio | -2.1803 |
| max_drawdown | 0.9359 |
| cagr | -0.6538 |
| net_avg_win | 27.4042 |
| net_avg_loss | -44.1059 |
| avg_hold_time_bars | 7.0191 |
| exposure | 0.2339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
