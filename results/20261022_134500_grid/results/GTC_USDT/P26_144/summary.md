# EMA Hourly Continuation — GTC/USDT P26_144

**Symbol:** GTC/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.6134 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.8501 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -3.6613 |
| sortino_ratio | -1.1668 |
| max_drawdown | 0.7621 |
| cagr | -0.4208 |
| net_avg_win | 52.1588 |
| net_avg_loss | -68.4506 |
| avg_hold_time_bars | 20.0354 |
| exposure | 0.4635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
