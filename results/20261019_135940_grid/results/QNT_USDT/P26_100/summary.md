# EMA Hourly Continuation — QNT/USDT P26_100

**Symbol:** QNT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 824 |
| net_profit_factor | 0.5390 |
| net_win_rate | 0.4842 |
| gross_profit_factor | 0.9407 |
| gross_win_rate | 0.4927 |
| sharpe_ratio | -5.1021 |
| sortino_ratio | -2.0589 |
| max_drawdown | 0.9232 |
| cagr | -0.6309 |
| net_avg_win | 26.9052 |
| net_avg_loss | -46.8627 |
| avg_hold_time_bars | 8.3883 |
| exposure | 0.3142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
