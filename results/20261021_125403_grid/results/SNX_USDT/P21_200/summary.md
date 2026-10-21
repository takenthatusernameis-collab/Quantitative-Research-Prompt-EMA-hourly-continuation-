# EMA Hourly Continuation — SNX/USDT P21_200

**Symbol:** SNX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.8765 |
| net_win_rate | 0.5120 |
| gross_profit_factor | 1.0528 |
| gross_win_rate | 0.5120 |
| sharpe_ratio | -0.7626 |
| sortino_ratio | -0.1991 |
| max_drawdown | 0.2809 |
| cagr | -0.0899 |
| net_avg_win | 88.3019 |
| net_avg_loss | -105.7242 |
| avg_hold_time_bars | 37.8946 |
| exposure | 0.5693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
