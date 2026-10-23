# EMA Hourly Continuation — CTSI/USDT P8_55

**Symbol:** CTSI/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1044 |
| net_profit_factor | 0.6454 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 1.0064 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -5.2094 |
| sortino_ratio | -2.3757 |
| max_drawdown | 0.9431 |
| cagr | -0.6767 |
| net_avg_win | 34.5411 |
| net_avg_loss | -48.4411 |
| avg_hold_time_bars | 9.9301 |
| exposure | 0.4712 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
