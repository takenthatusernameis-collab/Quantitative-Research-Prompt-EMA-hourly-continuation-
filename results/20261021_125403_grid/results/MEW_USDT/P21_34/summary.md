# EMA Hourly Continuation — MEW/USDT P21_34

**Symbol:** MEW/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.6153 |
| net_win_rate | 0.4518 |
| gross_profit_factor | 0.8233 |
| gross_win_rate | 0.4518 |
| sharpe_ratio | -2.8687 |
| sortino_ratio | -0.7447 |
| max_drawdown | 0.5786 |
| cagr | -0.2893 |
| net_avg_win | 61.3821 |
| net_avg_loss | -82.2247 |
| avg_hold_time_bars | 5.0904 |
| exposure | 0.0768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
