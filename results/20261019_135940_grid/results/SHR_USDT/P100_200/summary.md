# EMA Hourly Continuation — SHR/USDT P100_200

**Symbol:** SHR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 574 |
| net_profit_factor | 0.5077 |
| net_win_rate | 0.3833 |
| gross_profit_factor | 0.6927 |
| gross_win_rate | 0.3850 |
| sharpe_ratio | -5.7514 |
| sortino_ratio | -1.9237 |
| max_drawdown | 0.9078 |
| cagr | -0.6045 |
| net_avg_win | 42.3622 |
| net_avg_loss | -51.8541 |
| avg_hold_time_bars | 7.2944 |
| exposure | 0.1895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
