# EMA Hourly Continuation — XCN/USDT P89_200

**Symbol:** XCN/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.4668 |
| net_win_rate | 0.4224 |
| gross_profit_factor | 0.8075 |
| gross_win_rate | 0.4361 |
| sharpe_ratio | -5.4165 |
| sortino_ratio | -1.7103 |
| max_drawdown | 0.8834 |
| cagr | -0.5715 |
| net_avg_win | 35.8697 |
| net_avg_loss | -56.1965 |
| avg_hold_time_bars | 10.2417 |
| exposure | 0.2370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
