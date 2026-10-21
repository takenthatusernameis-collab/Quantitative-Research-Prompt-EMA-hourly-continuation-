# EMA Hourly Continuation — VET/USDT P34_144

**Symbol:** VET/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.8742 |
| net_win_rate | 0.5335 |
| gross_profit_factor | 1.1221 |
| gross_win_rate | 0.5335 |
| sharpe_ratio | -0.7467 |
| sortino_ratio | -0.2121 |
| max_drawdown | 0.2772 |
| cagr | -0.0958 |
| net_avg_win | 75.0249 |
| net_avg_loss | -98.1464 |
| avg_hold_time_bars | 20.2448 |
| exposure | 0.3570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
