# EMA Hourly Continuation — LSK/USDT P21_200

**Symbol:** LSK/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.7259 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9937 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.9969 |
| sortino_ratio | -0.5507 |
| max_drawdown | 0.5438 |
| cagr | -0.2269 |
| net_avg_win | 68.4853 |
| net_avg_loss | -90.4196 |
| avg_hold_time_bars | 34.7154 |
| exposure | 0.5933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
