# EMA Hourly Continuation — WOO/USDT P12_100

**Symbol:** WOO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.8393 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 1.0058 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -1.3787 |
| sortino_ratio | -0.4326 |
| max_drawdown | 0.4965 |
| cagr | -0.1824 |
| net_avg_win | 86.3893 |
| net_avg_loss | -102.0760 |
| avg_hold_time_bars | 26.6183 |
| exposure | 0.5832 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
