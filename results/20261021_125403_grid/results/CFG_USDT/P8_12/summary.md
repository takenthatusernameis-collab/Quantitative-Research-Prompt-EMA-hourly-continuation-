# EMA Hourly Continuation — CFG/USDT P8_12

**Symbol:** CFG/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.5383 |
| net_win_rate | 0.4332 |
| gross_profit_factor | 0.7309 |
| gross_win_rate | 0.4332 |
| sharpe_ratio | -2.9309 |
| sortino_ratio | -0.6935 |
| max_drawdown | 0.5663 |
| cagr | -0.2738 |
| net_avg_win | 53.6540 |
| net_avg_loss | -76.1844 |
| avg_hold_time_bars | 4.3285 |
| exposure | 0.0545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
