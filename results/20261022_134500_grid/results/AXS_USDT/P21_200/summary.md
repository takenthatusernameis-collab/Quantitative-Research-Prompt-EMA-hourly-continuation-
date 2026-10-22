# EMA Hourly Continuation — AXS/USDT P21_200

**Symbol:** AXS/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.7036 |
| net_win_rate | 0.4929 |
| gross_profit_factor | 1.0011 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -2.1623 |
| sortino_ratio | -0.5698 |
| max_drawdown | 0.5313 |
| cagr | -0.2394 |
| net_avg_win | 68.0147 |
| net_avg_loss | -93.9642 |
| avg_hold_time_bars | 39.5949 |
| exposure | 0.6325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
