# EMA Hourly Continuation — BONK/USDT P55_89

**Symbol:** BONK/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.8434 |
| net_win_rate | 0.5167 |
| gross_profit_factor | 1.0566 |
| gross_win_rate | 0.5167 |
| sharpe_ratio | -0.8309 |
| sortino_ratio | -0.1961 |
| max_drawdown | 0.2756 |
| cagr | -0.0876 |
| net_avg_win | 79.6888 |
| net_avg_loss | -101.0288 |
| avg_hold_time_bars | 7.2379 |
| exposure | 0.0885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
