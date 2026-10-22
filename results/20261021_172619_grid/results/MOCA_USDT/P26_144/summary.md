# EMA Hourly Continuation — MOCA/USDT P26_144

**Symbol:** MOCA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.7398 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.9100 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -1.9227 |
| sortino_ratio | -0.5234 |
| max_drawdown | 0.4319 |
| cagr | -0.2151 |
| net_avg_win | 76.2894 |
| net_avg_loss | -93.1016 |
| avg_hold_time_bars | 27.3694 |
| exposure | 0.4569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
