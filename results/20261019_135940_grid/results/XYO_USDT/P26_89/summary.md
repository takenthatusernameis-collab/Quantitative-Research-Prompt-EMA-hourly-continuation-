# EMA Hourly Continuation — XYO/USDT P26_89

**Symbol:** XYO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 785 |
| net_profit_factor | 0.4443 |
| net_win_rate | 0.4089 |
| gross_profit_factor | 0.8154 |
| gross_win_rate | 0.4229 |
| sharpe_ratio | -7.8767 |
| sortino_ratio | -3.0941 |
| max_drawdown | 0.9809 |
| cagr | -0.7891 |
| net_avg_win | 24.4149 |
| net_avg_loss | -38.0173 |
| avg_hold_time_bars | 9.0178 |
| exposure | 0.3203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
