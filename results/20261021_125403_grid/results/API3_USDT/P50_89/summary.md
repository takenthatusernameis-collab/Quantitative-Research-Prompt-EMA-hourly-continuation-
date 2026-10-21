# EMA Hourly Continuation — API3/USDT P50_89

**Symbol:** API3/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.7059 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9517 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -2.0762 |
| sortino_ratio | -0.5670 |
| max_drawdown | 0.5097 |
| cagr | -0.2289 |
| net_avg_win | 64.6394 |
| net_avg_loss | -87.6368 |
| avg_hold_time_bars | 8.5852 |
| exposure | 0.1420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
