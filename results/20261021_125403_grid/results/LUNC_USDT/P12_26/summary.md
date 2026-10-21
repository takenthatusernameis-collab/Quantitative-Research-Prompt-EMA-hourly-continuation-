# EMA Hourly Continuation — LUNC/USDT P12_26

**Symbol:** LUNC/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.6173 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.8858 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -3.0257 |
| sortino_ratio | -0.8569 |
| max_drawdown | 0.6270 |
| cagr | -0.3248 |
| net_avg_win | 55.2735 |
| net_avg_loss | -78.7748 |
| avg_hold_time_bars | 5.6036 |
| exposure | 0.0996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
