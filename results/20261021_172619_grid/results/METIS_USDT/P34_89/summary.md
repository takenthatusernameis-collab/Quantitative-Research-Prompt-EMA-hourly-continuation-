# EMA Hourly Continuation — METIS/USDT P34_89

**Symbol:** METIS/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.7509 |
| net_win_rate | 0.4837 |
| gross_profit_factor | 0.9597 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -2.0326 |
| sortino_ratio | -0.6021 |
| max_drawdown | 0.5344 |
| cagr | -0.2415 |
| net_avg_win | 72.5353 |
| net_avg_loss | -90.5080 |
| avg_hold_time_bars | 11.2163 |
| exposure | 0.2192 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
