# EMA Hourly Continuation — ARB/USDT P26_200

**Symbol:** ARB/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 1.0144 |
| net_win_rate | 0.5455 |
| gross_profit_factor | 1.1861 |
| gross_win_rate | 0.5455 |
| sharpe_ratio | 0.1300 |
| sortino_ratio | 0.0306 |
| max_drawdown | 0.1775 |
| cagr | 0.0081 |
| net_avg_win | 99.9930 |
| net_avg_loss | -118.2859 |
| avg_hold_time_bars | 49.3712 |
| exposure | 0.5925 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
