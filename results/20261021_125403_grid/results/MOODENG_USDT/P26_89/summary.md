# EMA Hourly Continuation — MOODENG/USDT P26_89

**Symbol:** MOODENG/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.7773 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9412 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -1.7866 |
| sortino_ratio | -0.5495 |
| max_drawdown | 0.4506 |
| cagr | -0.2247 |
| net_avg_win | 77.0541 |
| net_avg_loss | -93.0979 |
| avg_hold_time_bars | 14.5445 |
| exposure | 0.3074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
