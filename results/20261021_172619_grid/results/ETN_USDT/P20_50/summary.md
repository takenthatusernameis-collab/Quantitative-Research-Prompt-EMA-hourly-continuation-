# EMA Hourly Continuation — ETN/USDT P20_50

**Symbol:** ETN/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.5268 |
| net_win_rate | 0.4073 |
| gross_profit_factor | 0.6833 |
| gross_win_rate | 0.4073 |
| sharpe_ratio | -4.1659 |
| sortino_ratio | -1.2146 |
| max_drawdown | 0.6986 |
| cagr | -0.4297 |
| net_avg_win | 53.1780 |
| net_avg_loss | -69.3750 |
| avg_hold_time_bars | 9.5758 |
| exposure | 0.1852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
