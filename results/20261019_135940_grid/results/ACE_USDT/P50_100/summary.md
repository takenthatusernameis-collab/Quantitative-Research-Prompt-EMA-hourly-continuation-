# EMA Hourly Continuation — ACE/USDT P50_100

**Symbol:** ACE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.6248 |
| net_win_rate | 0.4941 |
| gross_profit_factor | 1.0278 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -3.1360 |
| sortino_ratio | -1.0001 |
| max_drawdown | 0.6989 |
| cagr | -0.3763 |
| net_avg_win | 45.9899 |
| net_avg_loss | -71.8962 |
| avg_hold_time_bars | 8.1961 |
| exposure | 0.1892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
