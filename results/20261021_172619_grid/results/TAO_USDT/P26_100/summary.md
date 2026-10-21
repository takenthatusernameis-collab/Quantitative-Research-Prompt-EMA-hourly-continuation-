# EMA Hourly Continuation — TAO/USDT P26_100

**Symbol:** TAO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.9390 |
| net_win_rate | 0.5293 |
| gross_profit_factor | 1.1150 |
| gross_win_rate | 0.5293 |
| sharpe_ratio | -0.3700 |
| sortino_ratio | -0.1103 |
| max_drawdown | 0.2559 |
| cagr | -0.0553 |
| net_avg_win | 90.6455 |
| net_avg_loss | -108.5425 |
| avg_hold_time_bars | 16.2576 |
| exposure | 0.3155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
