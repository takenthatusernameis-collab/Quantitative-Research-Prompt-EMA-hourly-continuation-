# EMA Hourly Continuation — DCR/USDT P20_144

**Symbol:** DCR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.6118 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 0.9144 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -3.2423 |
| sortino_ratio | -1.1152 |
| max_drawdown | 0.7506 |
| cagr | -0.4088 |
| net_avg_win | 40.0499 |
| net_avg_loss | -61.8263 |
| avg_hold_time_bars | 19.0874 |
| exposure | 0.5139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
