# EMA Hourly Continuation — XAI/USDT P12_144

**Symbol:** XAI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.7137 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.9846 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -2.9061 |
| sortino_ratio | -0.8627 |
| max_drawdown | 0.7164 |
| cagr | -0.3405 |
| net_avg_win | 76.6075 |
| net_avg_loss | -95.5663 |
| avg_hold_time_bars | 35.5692 |
| exposure | 0.7243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
