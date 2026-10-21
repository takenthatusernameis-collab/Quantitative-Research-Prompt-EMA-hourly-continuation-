# EMA Hourly Continuation — ICP/USDT P34_200

**Symbol:** ICP/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.8319 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 0.9969 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -0.9230 |
| sortino_ratio | -0.2248 |
| max_drawdown | 0.2647 |
| cagr | -0.0998 |
| net_avg_win | 78.6292 |
| net_avg_loss | -95.8337 |
| avg_hold_time_bars | 35.9655 |
| exposure | 0.4741 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
