# EMA Hourly Continuation — CHZ/USDT P12_100

**Symbol:** CHZ/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.6946 |
| net_win_rate | 0.5024 |
| gross_profit_factor | 1.0363 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -2.9043 |
| sortino_ratio | -1.0135 |
| max_drawdown | 0.7134 |
| cagr | -0.3876 |
| net_avg_win | 51.9419 |
| net_avg_loss | -75.5151 |
| avg_hold_time_bars | 20.5511 |
| exposure | 0.5764 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
