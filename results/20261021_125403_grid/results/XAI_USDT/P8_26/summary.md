# EMA Hourly Continuation — XAI/USDT P8_26

**Symbol:** XAI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 745 |
| net_profit_factor | 0.7684 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9952 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -2.4810 |
| sortino_ratio | -0.9702 |
| max_drawdown | 0.7011 |
| cagr | -0.3593 |
| net_avg_win | 60.1920 |
| net_avg_loss | -77.7069 |
| avg_hold_time_bars | 6.4134 |
| exposure | 0.2172 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
