# EMA Hourly Continuation — CHR/USDT P100_144

**Symbol:** CHR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.7648 |
| net_win_rate | 0.5085 |
| gross_profit_factor | 1.0193 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -1.3659 |
| sortino_ratio | -0.3366 |
| max_drawdown | 0.3813 |
| cagr | -0.1428 |
| net_avg_win | 69.8153 |
| net_avg_loss | -94.4360 |
| avg_hold_time_bars | 7.1288 |
| exposure | 0.0952 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
