# EMA Hourly Continuation — SAFE/USDT P34_89

**Symbol:** SAFE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.8809 |
| net_win_rate | 0.5300 |
| gross_profit_factor | 1.1149 |
| gross_win_rate | 0.5300 |
| sharpe_ratio | -0.7746 |
| sortino_ratio | -0.2337 |
| max_drawdown | 0.3251 |
| cagr | -0.1053 |
| net_avg_win | 77.8812 |
| net_avg_loss | -99.6756 |
| avg_hold_time_bars | 12.6843 |
| exposure | 0.2521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
