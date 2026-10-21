# EMA Hourly Continuation — XNO/USDT P26_200

**Symbol:** XNO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.6706 |
| net_win_rate | 0.4467 |
| gross_profit_factor | 0.8213 |
| gross_win_rate | 0.4467 |
| sharpe_ratio | -2.6299 |
| sortino_ratio | -0.7479 |
| max_drawdown | 0.5789 |
| cagr | -0.2913 |
| net_avg_win | 65.4745 |
| net_avg_loss | -78.8080 |
| avg_hold_time_bars | 28.0149 |
| exposure | 0.5132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
