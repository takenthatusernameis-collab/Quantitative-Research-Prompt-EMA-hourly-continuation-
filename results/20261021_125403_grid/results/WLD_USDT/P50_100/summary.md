# EMA Hourly Continuation — WLD/USDT P50_100

**Symbol:** WLD/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.8232 |
| net_win_rate | 0.5060 |
| gross_profit_factor | 1.0151 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -1.0744 |
| sortino_ratio | -0.2826 |
| max_drawdown | 0.2851 |
| cagr | -0.1230 |
| net_avg_win | 76.9346 |
| net_avg_loss | -95.7070 |
| avg_hold_time_bars | 9.6607 |
| exposure | 0.1475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
