# EMA Hourly Continuation — SEI/USDT P89_144

**Symbol:** SEI/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.5193 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.8298 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -4.2509 |
| sortino_ratio | -1.2752 |
| max_drawdown | 0.8068 |
| cagr | -0.4595 |
| net_avg_win | 41.0472 |
| net_avg_loss | -67.0635 |
| avg_hold_time_bars | 4.9002 |
| exposure | 0.1005 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
