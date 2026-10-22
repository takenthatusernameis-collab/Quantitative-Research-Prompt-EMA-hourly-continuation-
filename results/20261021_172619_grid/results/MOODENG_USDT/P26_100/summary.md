# EMA Hourly Continuation — MOODENG/USDT P26_100

**Symbol:** MOODENG/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.7670 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9127 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -1.7866 |
| sortino_ratio | -0.5326 |
| max_drawdown | 0.4254 |
| cagr | -0.2186 |
| net_avg_win | 76.3191 |
| net_avg_loss | -91.0381 |
| avg_hold_time_bars | 17.4472 |
| exposure | 0.3475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
