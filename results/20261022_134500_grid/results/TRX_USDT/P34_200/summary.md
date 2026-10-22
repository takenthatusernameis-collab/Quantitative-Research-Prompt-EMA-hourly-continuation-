# EMA Hourly Continuation — TRX/USDT P34_200

**Symbol:** TRX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.3551 |
| net_win_rate | 0.4261 |
| gross_profit_factor | 0.8915 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -6.2200 |
| sortino_ratio | -1.7467 |
| max_drawdown | 0.9080 |
| cagr | -0.6111 |
| net_avg_win | 28.8595 |
| net_avg_loss | -60.3401 |
| avg_hold_time_bars | 22.0837 |
| exposure | 0.4075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
