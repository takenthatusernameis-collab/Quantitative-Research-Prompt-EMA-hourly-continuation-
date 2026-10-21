# EMA Hourly Continuation — ZRO/USDT P21_89

**Symbol:** ZRO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.8771 |
| net_win_rate | 0.5119 |
| gross_profit_factor | 1.0375 |
| gross_win_rate | 0.5119 |
| sharpe_ratio | -0.8499 |
| sortino_ratio | -0.2725 |
| max_drawdown | 0.3049 |
| cagr | -0.1217 |
| net_avg_win | 78.5989 |
| net_avg_loss | -93.9782 |
| avg_hold_time_bars | 15.2700 |
| exposure | 0.3460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
