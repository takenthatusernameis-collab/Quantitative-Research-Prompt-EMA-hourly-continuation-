# EMA Hourly Continuation — ENA/USDT P26_144

**Symbol:** ENA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.7131 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9302 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -2.1865 |
| sortino_ratio | -0.6807 |
| max_drawdown | 0.5747 |
| cagr | -0.2751 |
| net_avg_win | 58.6139 |
| net_avg_loss | -76.6536 |
| avg_hold_time_bars | 21.1068 |
| exposure | 0.4672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
