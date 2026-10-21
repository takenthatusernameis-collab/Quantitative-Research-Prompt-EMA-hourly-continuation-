# EMA Hourly Continuation — KCS/USDT P8_20

**Symbol:** KCS/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.3716 |
| net_win_rate | 0.4336 |
| gross_profit_factor | 0.7465 |
| gross_win_rate | 0.4414 |
| sharpe_ratio | -6.2695 |
| sortino_ratio | -2.0553 |
| max_drawdown | 0.9147 |
| cagr | -0.6203 |
| net_avg_win | 24.2989 |
| net_avg_loss | -50.0536 |
| avg_hold_time_bars | 7.3262 |
| exposure | 0.1705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
