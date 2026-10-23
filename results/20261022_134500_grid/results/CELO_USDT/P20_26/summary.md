# EMA Hourly Continuation — CELO/USDT P20_26

**Symbol:** CELO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1209 |
| net_profit_factor | 0.2038 |
| net_win_rate | 0.3854 |
| gross_profit_factor | 0.6040 |
| gross_win_rate | 0.4285 |
| sharpe_ratio | -13.2827 |
| sortino_ratio | -6.6319 |
| max_drawdown | 0.9999 |
| cagr | -0.9698 |
| net_avg_win | 5.4918 |
| net_avg_loss | -16.9014 |
| avg_hold_time_bars | 2.1183 |
| exposure | 0.1159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
