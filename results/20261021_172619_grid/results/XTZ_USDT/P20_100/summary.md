# EMA Hourly Continuation — XTZ/USDT P20_100

**Symbol:** XTZ/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.7821 |
| net_win_rate | 0.5072 |
| gross_profit_factor | 1.0362 |
| gross_win_rate | 0.5072 |
| sharpe_ratio | -1.7438 |
| sortino_ratio | -0.5527 |
| max_drawdown | 0.4925 |
| cagr | -0.2245 |
| net_avg_win | 68.5681 |
| net_avg_loss | -90.2303 |
| avg_hold_time_bars | 20.7372 |
| exposure | 0.4590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
