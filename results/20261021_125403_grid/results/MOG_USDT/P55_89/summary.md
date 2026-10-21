# EMA Hourly Continuation — MOG/USDT P55_89

**Symbol:** MOG/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.6981 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.8784 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -1.9424 |
| sortino_ratio | -0.4773 |
| max_drawdown | 0.4270 |
| cagr | -0.1966 |
| net_avg_win | 71.3705 |
| net_avg_loss | -90.8777 |
| avg_hold_time_bars | 6.2316 |
| exposure | 0.0843 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
