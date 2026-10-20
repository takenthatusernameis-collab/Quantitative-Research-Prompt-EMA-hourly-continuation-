# EMA Hourly Continuation — TNSR/USDT P8_34

**Symbol:** TNSR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1300 |
| net_profit_factor | 0.6865 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 1.0574 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -6.0636 |
| sortino_ratio | -3.0666 |
| max_drawdown | 0.9767 |
| cagr | -0.7725 |
| net_avg_win | 34.3699 |
| net_avg_loss | -45.9280 |
| avg_hold_time_bars | 6.0962 |
| exposure | 0.3586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
