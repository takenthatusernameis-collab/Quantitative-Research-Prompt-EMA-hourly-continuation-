# EMA Hourly Continuation — ARKM/USDT P12_89

**Symbol:** ARKM/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 738 |
| net_profit_factor | 0.5811 |
| net_win_rate | 0.4526 |
| gross_profit_factor | 0.8501 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -4.5080 |
| sortino_ratio | -1.7258 |
| max_drawdown | 0.8739 |
| cagr | -0.5575 |
| net_avg_win | 36.1811 |
| net_avg_loss | -51.4705 |
| avg_hold_time_bars | 16.0352 |
| exposure | 0.5379 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
