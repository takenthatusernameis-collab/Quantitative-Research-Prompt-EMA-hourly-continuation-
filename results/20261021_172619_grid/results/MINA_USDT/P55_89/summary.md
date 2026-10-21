# EMA Hourly Continuation — MINA/USDT P55_89

**Symbol:** MINA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.7501 |
| net_win_rate | 0.5175 |
| gross_profit_factor | 1.0617 |
| gross_win_rate | 0.5175 |
| sharpe_ratio | -1.7028 |
| sortino_ratio | -0.4724 |
| max_drawdown | 0.4645 |
| cagr | -0.1942 |
| net_avg_win | 65.4398 |
| net_avg_loss | -93.5733 |
| avg_hold_time_bars | 6.2884 |
| exposure | 0.1060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
