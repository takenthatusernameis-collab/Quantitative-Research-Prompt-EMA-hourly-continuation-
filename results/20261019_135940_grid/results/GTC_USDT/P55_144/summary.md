# EMA Hourly Continuation — GTC/USDT P55_144

**Symbol:** GTC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.5872 |
| net_win_rate | 0.4600 |
| gross_profit_factor | 0.8635 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -3.5180 |
| sortino_ratio | -1.0978 |
| max_drawdown | 0.7380 |
| cagr | -0.4020 |
| net_avg_win | 46.0336 |
| net_avg_loss | -66.7757 |
| avg_hold_time_bars | 12.4292 |
| exposure | 0.2751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
