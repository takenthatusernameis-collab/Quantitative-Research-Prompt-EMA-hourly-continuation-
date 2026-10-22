# EMA Hourly Continuation — AXS/USDT P50_100

**Symbol:** AXS/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.5852 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 1.0054 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -4.1155 |
| sortino_ratio | -1.3887 |
| max_drawdown | 0.8252 |
| cagr | -0.4848 |
| net_avg_win | 41.2167 |
| net_avg_loss | -67.5223 |
| avg_hold_time_bars | 6.3451 |
| exposure | 0.1631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
