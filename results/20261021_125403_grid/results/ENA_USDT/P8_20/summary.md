# EMA Hourly Continuation — ENA/USDT P8_20

**Symbol:** ENA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.9491 |
| net_win_rate | 0.5476 |
| gross_profit_factor | 1.1981 |
| gross_win_rate | 0.5476 |
| sharpe_ratio | -0.2876 |
| sortino_ratio | -0.0897 |
| max_drawdown | 0.2424 |
| cagr | -0.0470 |
| net_avg_win | 84.0072 |
| net_avg_loss | -107.1462 |
| avg_hold_time_bars | 5.5866 |
| exposure | 0.1173 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
