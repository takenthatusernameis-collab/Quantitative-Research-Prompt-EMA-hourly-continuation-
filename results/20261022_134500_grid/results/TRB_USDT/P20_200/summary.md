# EMA Hourly Continuation — TRB/USDT P20_200

**Symbol:** TRB/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.5979 |
| net_win_rate | 0.4478 |
| gross_profit_factor | 0.8264 |
| gross_win_rate | 0.4533 |
| sharpe_ratio | -3.1240 |
| sortino_ratio | -0.8311 |
| max_drawdown | 0.6401 |
| cagr | -0.3288 |
| net_avg_win | 57.8668 |
| net_avg_loss | -78.4820 |
| avg_hold_time_bars | 40.9231 |
| exposure | 0.6741 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
