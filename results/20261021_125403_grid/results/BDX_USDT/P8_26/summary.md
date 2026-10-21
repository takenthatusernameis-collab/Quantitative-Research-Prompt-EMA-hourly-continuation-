# EMA Hourly Continuation — BDX/USDT P8_26

**Symbol:** BDX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.4141 |
| net_win_rate | 0.3599 |
| gross_profit_factor | 0.6871 |
| gross_win_rate | 0.3625 |
| sharpe_ratio | -6.3670 |
| sortino_ratio | -1.8036 |
| max_drawdown | 0.8884 |
| cagr | -0.5744 |
| net_avg_win | 44.5681 |
| net_avg_loss | -60.5184 |
| avg_hold_time_bars | 5.1877 |
| exposure | 0.0917 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
