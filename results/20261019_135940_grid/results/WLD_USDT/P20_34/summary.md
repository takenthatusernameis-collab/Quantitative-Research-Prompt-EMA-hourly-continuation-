# EMA Hourly Continuation — WLD/USDT P20_34

**Symbol:** WLD/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1128 |
| net_profit_factor | 0.4647 |
| net_win_rate | 0.4628 |
| gross_profit_factor | 0.8844 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -7.9476 |
| sortino_ratio | -3.7506 |
| max_drawdown | 0.9912 |
| cagr | -0.8467 |
| net_avg_win | 16.4829 |
| net_avg_loss | -30.5513 |
| avg_hold_time_bars | 2.5479 |
| exposure | 0.1306 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
