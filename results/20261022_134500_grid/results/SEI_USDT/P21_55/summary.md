# EMA Hourly Continuation — SEI/USDT P21_55

**Symbol:** SEI/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 919 |
| net_profit_factor | 0.5825 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.9636 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -5.8916 |
| sortino_ratio | -2.5016 |
| max_drawdown | 0.9571 |
| cagr | -0.7068 |
| net_avg_win | 30.5258 |
| net_avg_loss | -47.3086 |
| avg_hold_time_bars | 5.2035 |
| exposure | 0.2174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
