# EMA Hourly Continuation — KNC/USDT P12_200

**Symbol:** KNC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.7725 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9669 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -1.2773 |
| sortino_ratio | -0.2964 |
| max_drawdown | 0.3666 |
| cagr | -0.1279 |
| net_avg_win | 76.5575 |
| net_avg_loss | -94.7001 |
| avg_hold_time_bars | 66.5606 |
| exposure | 0.7987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
