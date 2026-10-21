# EMA Hourly Continuation — XRP/USDT P50_89

**Symbol:** XRP/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.5483 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.8747 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -2.9732 |
| sortino_ratio | -0.7315 |
| max_drawdown | 0.5738 |
| cagr | -0.2829 |
| net_avg_win | 49.4466 |
| net_avg_loss | -81.3957 |
| avg_hold_time_bars | 8.7918 |
| exposure | 0.1171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
