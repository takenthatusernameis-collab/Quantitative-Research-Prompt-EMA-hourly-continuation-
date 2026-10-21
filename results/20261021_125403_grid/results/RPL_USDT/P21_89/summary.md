# EMA Hourly Continuation — RPL/USDT P21_89

**Symbol:** RPL/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.7469 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9326 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -2.2085 |
| sortino_ratio | -0.7277 |
| max_drawdown | 0.5861 |
| cagr | -0.2847 |
| net_avg_win | 65.5096 |
| net_avg_loss | -80.7946 |
| avg_hold_time_bars | 16.0914 |
| exposure | 0.3903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
