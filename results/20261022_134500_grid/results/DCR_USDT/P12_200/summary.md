# EMA Hourly Continuation — DCR/USDT P12_200

**Symbol:** DCR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.7136 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 1.0117 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -2.4771 |
| sortino_ratio | -0.7959 |
| max_drawdown | 0.6388 |
| cagr | -0.3132 |
| net_avg_win | 59.3844 |
| net_avg_loss | -81.0081 |
| avg_hold_time_bars | 28.6008 |
| exposure | 0.6743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
