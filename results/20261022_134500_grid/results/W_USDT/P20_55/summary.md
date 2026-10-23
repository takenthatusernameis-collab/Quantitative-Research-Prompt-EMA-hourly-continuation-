# EMA Hourly Continuation — W/USDT P20_55

**Symbol:** W/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 925 |
| net_profit_factor | 0.5956 |
| net_win_rate | 0.4551 |
| gross_profit_factor | 0.9414 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -6.0123 |
| sortino_ratio | -2.5692 |
| max_drawdown | 0.9577 |
| cagr | -0.7134 |
| net_avg_win | 33.4727 |
| net_avg_loss | -46.9412 |
| avg_hold_time_bars | 5.6951 |
| exposure | 0.2395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
