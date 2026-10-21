# EMA Hourly Continuation — MOODENG/USDT P144_200

**Symbol:** MOODENG/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 174 |
| net_profit_factor | 0.7362 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9288 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -1.4073 |
| sortino_ratio | -0.2923 |
| max_drawdown | 0.2627 |
| cagr | -0.1262 |
| net_avg_win | 80.6978 |
| net_avg_loss | -102.3069 |
| avg_hold_time_bars | 7.1207 |
| exposure | 0.0686 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
