# EMA Hourly Continuation — WLD/USDT P26_200

**Symbol:** WLD/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 1.0462 |
| net_win_rate | 0.5420 |
| gross_profit_factor | 1.1706 |
| gross_win_rate | 0.5420 |
| sharpe_ratio | 0.2848 |
| sortino_ratio | 0.0668 |
| max_drawdown | 0.1462 |
| cagr | 0.0242 |
| net_avg_win | 98.4640 |
| net_avg_loss | -111.3679 |
| avg_hold_time_bars | 48.6794 |
| exposure | 0.5797 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
