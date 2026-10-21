# EMA Hourly Continuation — BTT/USDT P89_200

**Symbol:** BTT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.5240 |
| net_win_rate | 0.4458 |
| gross_profit_factor | 0.8505 |
| gross_win_rate | 0.4458 |
| sharpe_ratio | -3.5114 |
| sortino_ratio | -0.7808 |
| max_drawdown | 0.6031 |
| cagr | -0.3060 |
| net_avg_win | 61.7784 |
| net_avg_loss | -94.8455 |
| avg_hold_time_bars | 21.1458 |
| exposure | 0.2307 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
