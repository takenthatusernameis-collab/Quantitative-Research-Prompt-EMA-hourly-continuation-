# EMA Hourly Continuation — ERG/USDT P26_50

**Symbol:** ERG/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.5736 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.7976 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -3.1001 |
| sortino_ratio | -0.7979 |
| max_drawdown | 0.6112 |
| cagr | -0.3063 |
| net_avg_win | 55.7472 |
| net_avg_loss | -77.8522 |
| avg_hold_time_bars | 7.9387 |
| exposure | 0.1176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
