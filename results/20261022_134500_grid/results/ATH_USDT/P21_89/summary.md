# EMA Hourly Continuation — ATH/USDT P21_89

**Symbol:** ATH/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 708 |
| net_profit_factor | 0.7075 |
| net_win_rate | 0.5099 |
| gross_profit_factor | 1.0467 |
| gross_win_rate | 0.5155 |
| sharpe_ratio | -2.9481 |
| sortino_ratio | -1.1480 |
| max_drawdown | 0.7413 |
| cagr | -0.4191 |
| net_avg_win | 48.3653 |
| net_avg_loss | -71.1145 |
| avg_hold_time_bars | 9.7133 |
| exposure | 0.3333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
