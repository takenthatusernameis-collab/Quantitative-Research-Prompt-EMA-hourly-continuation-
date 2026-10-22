# EMA Hourly Continuation — AXS/USDT P12_89

**Symbol:** AXS/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.6720 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 1.0012 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -3.6390 |
| sortino_ratio | -1.3476 |
| max_drawdown | 0.8126 |
| cagr | -0.4746 |
| net_avg_win | 49.3924 |
| net_avg_loss | -68.1764 |
| avg_hold_time_bars | 16.6214 |
| exposure | 0.5205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
