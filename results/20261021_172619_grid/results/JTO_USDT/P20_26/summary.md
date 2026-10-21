# EMA Hourly Continuation — JTO/USDT P20_26

**Symbol:** JTO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.7439 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0132 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.5402 |
| sortino_ratio | -0.3591 |
| max_drawdown | 0.4079 |
| cagr | -0.1519 |
| net_avg_win | 74.5696 |
| net_avg_loss | -100.2435 |
| avg_hold_time_bars | 4.8523 |
| exposure | 0.0582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
