# EMA Hourly Continuation — GRT/USDT P21_26

**Symbol:** GRT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1172 |
| net_profit_factor | 0.2348 |
| net_win_rate | 0.3302 |
| gross_profit_factor | 0.6858 |
| gross_win_rate | 0.3840 |
| sharpe_ratio | -15.3184 |
| sortino_ratio | -7.6969 |
| max_drawdown | 1.0000 |
| cagr | -0.9838 |
| net_avg_win | 7.9286 |
| net_avg_loss | -16.6472 |
| avg_hold_time_bars | 1.8012 |
| exposure | 0.0955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
