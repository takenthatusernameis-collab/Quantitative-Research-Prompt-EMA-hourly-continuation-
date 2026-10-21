# EMA Hourly Continuation — SEI/USDT P20_55

**Symbol:** SEI/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.7922 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 1.0104 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -1.6633 |
| sortino_ratio | -0.5200 |
| max_drawdown | 0.4758 |
| cagr | -0.2127 |
| net_avg_win | 72.3099 |
| net_avg_loss | -91.6643 |
| avg_hold_time_bars | 9.7095 |
| exposure | 0.2096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
