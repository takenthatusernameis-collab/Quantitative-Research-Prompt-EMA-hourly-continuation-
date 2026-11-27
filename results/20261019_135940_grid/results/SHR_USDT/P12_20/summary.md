# EMA Hourly Continuation — SHR/USDT P12_20

**Symbol:** SHR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1711 |
| net_profit_factor | 0.3070 |
| net_win_rate | 0.2981 |
| gross_profit_factor | 0.6100 |
| gross_win_rate | 0.3057 |
| sharpe_ratio | -17.3110 |
| sortino_ratio | -10.1401 |
| max_drawdown | 1.0000 |
| cagr | -0.9944 |
| net_avg_win | 8.6882 |
| net_avg_loss | -12.0158 |
| avg_hold_time_bars | 2.2963 |
| exposure | 0.1778 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
