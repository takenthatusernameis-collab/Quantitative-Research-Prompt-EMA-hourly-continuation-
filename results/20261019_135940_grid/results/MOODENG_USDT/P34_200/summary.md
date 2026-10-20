# EMA Hourly Continuation — MOODENG/USDT P34_200

**Symbol:** MOODENG/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.8440 |
| net_win_rate | 0.5164 |
| gross_profit_factor | 1.0887 |
| gross_win_rate | 0.5197 |
| sharpe_ratio | -1.0956 |
| sortino_ratio | -0.2998 |
| max_drawdown | 0.3398 |
| cagr | -0.1332 |
| net_avg_win | 88.0486 |
| net_avg_loss | -111.4170 |
| avg_hold_time_bars | 31.6283 |
| exposure | 0.5320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
