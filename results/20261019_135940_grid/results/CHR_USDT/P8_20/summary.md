# EMA Hourly Continuation — CHR/USDT P8_20

**Symbol:** CHR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1578 |
| net_profit_factor | 0.3975 |
| net_win_rate | 0.4278 |
| gross_profit_factor | 0.8256 |
| gross_win_rate | 0.4474 |
| sharpe_ratio | -10.4661 |
| sortino_ratio | -5.8635 |
| max_drawdown | 0.9993 |
| cagr | -0.9431 |
| net_avg_win | 9.7651 |
| net_avg_loss | -18.3656 |
| avg_hold_time_bars | 3.5450 |
| exposure | 0.2531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
