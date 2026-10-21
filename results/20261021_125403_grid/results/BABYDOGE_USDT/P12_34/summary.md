# EMA Hourly Continuation — BABYDOGE/USDT P12_34

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 44 |
| net_profit_factor | 0.6319 |
| net_win_rate | 0.4091 |
| gross_profit_factor | 0.6906 |
| gross_win_rate | 0.4091 |
| sharpe_ratio | -0.9403 |
| sortino_ratio | -0.0872 |
| max_drawdown | 0.1097 |
| cagr | -0.0395 |
| net_avg_win | 92.2067 |
| net_avg_loss | -101.0232 |
| avg_hold_time_bars | 8.5682 |
| exposure | 0.0171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
