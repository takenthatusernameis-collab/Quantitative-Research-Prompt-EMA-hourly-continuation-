# EMA Hourly Continuation — ZIL/USDT P50_55

**Symbol:** ZIL/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 123 |
| net_profit_factor | 0.7117 |
| net_win_rate | 0.5203 |
| gross_profit_factor | 1.0714 |
| gross_win_rate | 0.5203 |
| sharpe_ratio | -1.1361 |
| sortino_ratio | -0.1819 |
| max_drawdown | 0.2641 |
| cagr | -0.0801 |
| net_avg_win | 72.9090 |
| net_avg_loss | -111.1323 |
| avg_hold_time_bars | 4.7805 |
| exposure | 0.0267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
