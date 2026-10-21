# EMA Hourly Continuation — RAY/USDT P21_100

**Symbol:** RAY/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.8567 |
| net_win_rate | 0.5077 |
| gross_profit_factor | 1.0322 |
| gross_win_rate | 0.5077 |
| sharpe_ratio | -1.0516 |
| sortino_ratio | -0.3224 |
| max_drawdown | 0.3967 |
| cagr | -0.1403 |
| net_avg_win | 81.4103 |
| net_avg_loss | -97.9836 |
| avg_hold_time_bars | 17.2867 |
| exposure | 0.3591 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
