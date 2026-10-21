# EMA Hourly Continuation — IMX/USDT P8_50

**Symbol:** IMX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.8429 |
| net_win_rate | 0.5125 |
| gross_profit_factor | 1.0373 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -1.3242 |
| sortino_ratio | -0.4946 |
| max_drawdown | 0.4788 |
| cagr | -0.2067 |
| net_avg_win | 68.1945 |
| net_avg_loss | -85.0600 |
| avg_hold_time_bars | 14.4669 |
| exposure | 0.4445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
