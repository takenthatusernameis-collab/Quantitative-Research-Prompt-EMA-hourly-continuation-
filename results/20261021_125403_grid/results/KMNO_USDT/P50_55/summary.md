# EMA Hourly Continuation — KMNO/USDT P50_55

**Symbol:** KMNO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 150 |
| net_profit_factor | 0.6745 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0039 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.5382 |
| sortino_ratio | -0.2719 |
| max_drawdown | 0.3126 |
| cagr | -0.1181 |
| net_avg_win | 73.8096 |
| net_avg_loss | -109.4267 |
| avg_hold_time_bars | 6.3067 |
| exposure | 0.0437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
