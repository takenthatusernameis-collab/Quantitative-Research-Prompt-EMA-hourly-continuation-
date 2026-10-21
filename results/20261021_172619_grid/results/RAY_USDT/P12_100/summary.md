# EMA Hourly Continuation — RAY/USDT P12_100

**Symbol:** RAY/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.8589 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0154 |
| gross_win_rate | 0.5042 |
| sharpe_ratio | -1.0466 |
| sortino_ratio | -0.3278 |
| max_drawdown | 0.3893 |
| cagr | -0.1429 |
| net_avg_win | 81.1250 |
| net_avg_loss | -96.0411 |
| avg_hold_time_bars | 24.2887 |
| exposure | 0.5277 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
