# EMA Hourly Continuation — STX/USDT P21_26

**Symbol:** STX/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 166 |
| net_profit_factor | 0.7699 |
| net_win_rate | 0.5241 |
| gross_profit_factor | 1.0792 |
| gross_win_rate | 0.5241 |
| sharpe_ratio | -0.9819 |
| sortino_ratio | -0.1823 |
| max_drawdown | 0.2696 |
| cagr | -0.0799 |
| net_avg_win | 72.8368 |
| net_avg_loss | -104.1902 |
| avg_hold_time_bars | 5.3494 |
| exposure | 0.0402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
