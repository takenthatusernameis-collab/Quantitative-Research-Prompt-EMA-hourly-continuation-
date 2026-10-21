# EMA Hourly Continuation — AURORA/USDT P144_200

**Symbol:** AURORA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 159 |
| net_profit_factor | 1.0656 |
| net_win_rate | 0.6101 |
| gross_profit_factor | 1.5490 |
| gross_win_rate | 0.6101 |
| sharpe_ratio | 0.2935 |
| sortino_ratio | 0.0545 |
| max_drawdown | 0.1041 |
| cagr | 0.0203 |
| net_avg_win | 86.6631 |
| net_avg_loss | -127.2388 |
| avg_hold_time_bars | 7.5157 |
| exposure | 0.0543 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
