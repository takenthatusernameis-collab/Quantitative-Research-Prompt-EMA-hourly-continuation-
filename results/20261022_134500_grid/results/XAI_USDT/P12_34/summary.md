# EMA Hourly Continuation — XAI/USDT P12_34

**Symbol:** XAI/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1366 |
| net_profit_factor | 0.5874 |
| net_win_rate | 0.4246 |
| gross_profit_factor | 0.9432 |
| gross_win_rate | 0.4429 |
| sharpe_ratio | -9.1137 |
| sortino_ratio | -4.7508 |
| max_drawdown | 0.9971 |
| cagr | -0.9005 |
| net_avg_win | 24.4728 |
| net_avg_loss | -30.7427 |
| avg_hold_time_bars | 4.3119 |
| exposure | 0.2677 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
