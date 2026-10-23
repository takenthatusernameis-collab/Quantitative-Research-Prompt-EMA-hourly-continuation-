# EMA Hourly Continuation — RPL/USDT P21_55

**Symbol:** RPL/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 892 |
| net_profit_factor | 0.5447 |
| net_win_rate | 0.4529 |
| gross_profit_factor | 0.9280 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -6.0068 |
| sortino_ratio | -2.5164 |
| max_drawdown | 0.9547 |
| cagr | -0.7035 |
| net_avg_win | 28.2381 |
| net_avg_loss | -42.9143 |
| avg_hold_time_bars | 6.4731 |
| exposure | 0.2613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
