# EMA Hourly Continuation — XDC/USDT P12_55

**Symbol:** XDC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1118 |
| net_profit_factor | 0.2518 |
| net_win_rate | 0.4070 |
| gross_profit_factor | 0.6595 |
| gross_win_rate | 0.4454 |
| sharpe_ratio | -10.8232 |
| sortino_ratio | -5.0866 |
| max_drawdown | 0.9987 |
| cagr | -0.9294 |
| net_avg_win | 7.3879 |
| net_avg_loss | -20.1336 |
| avg_hold_time_bars | 6.6825 |
| exposure | 0.3396 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
