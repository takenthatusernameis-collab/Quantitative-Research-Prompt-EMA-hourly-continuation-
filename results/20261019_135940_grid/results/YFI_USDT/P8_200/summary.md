# EMA Hourly Continuation — YFI/USDT P8_200

**Symbol:** YFI/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.5502 |
| net_win_rate | 0.4625 |
| gross_profit_factor | 0.8873 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -3.5078 |
| sortino_ratio | -0.9801 |
| max_drawdown | 0.7079 |
| cagr | -0.3789 |
| net_avg_win | 46.2372 |
| net_avg_loss | -72.3081 |
| avg_hold_time_bars | 44.2125 |
| exposure | 0.8003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
