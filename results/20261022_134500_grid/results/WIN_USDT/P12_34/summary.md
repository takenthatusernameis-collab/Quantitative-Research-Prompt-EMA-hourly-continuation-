# EMA Hourly Continuation — WIN/USDT P12_34

**Symbol:** WIN/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1255 |
| net_profit_factor | 0.2880 |
| net_win_rate | 0.4072 |
| gross_profit_factor | 0.7676 |
| gross_win_rate | 0.4311 |
| sharpe_ratio | -12.1873 |
| sortino_ratio | -6.1805 |
| max_drawdown | 0.9996 |
| cagr | -0.9577 |
| net_avg_win | 7.9112 |
| net_avg_loss | -18.8697 |
| avg_hold_time_bars | 4.4343 |
| exposure | 0.2530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
