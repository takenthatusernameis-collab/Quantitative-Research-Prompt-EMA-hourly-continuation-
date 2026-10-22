# EMA Hourly Continuation — SLP/USDT P50_200

**Symbol:** SLP/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.8003 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 0.9869 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -1.2023 |
| sortino_ratio | -0.3082 |
| max_drawdown | 0.3092 |
| cagr | -0.1333 |
| net_avg_win | 75.6096 |
| net_avg_loss | -93.8924 |
| avg_hold_time_bars | 27.5421 |
| exposure | 0.4019 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
