# EMA Hourly Continuation — IMX/USDT P26_100

**Symbol:** IMX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.6403 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9147 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -3.1458 |
| sortino_ratio | -1.0916 |
| max_drawdown | 0.7335 |
| cagr | -0.4059 |
| net_avg_win | 44.1255 |
| net_avg_loss | -64.7402 |
| avg_hold_time_bars | 13.2282 |
| exposure | 0.3645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
