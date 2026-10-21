# EMA Hourly Continuation — 1INCH/USDT P20_100

**Symbol:** 1INCH/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.6638 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.8593 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -2.8006 |
| sortino_ratio | -0.8305 |
| max_drawdown | 0.6332 |
| cagr | -0.3175 |
| net_avg_win | 60.9035 |
| net_avg_loss | -78.4143 |
| avg_hold_time_bars | 24.3479 |
| exposure | 0.4803 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
