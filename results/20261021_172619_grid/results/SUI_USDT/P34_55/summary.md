# EMA Hourly Continuation — SUI/USDT P34_55

**Symbol:** SUI/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.9761 |
| net_win_rate | 0.5714 |
| gross_profit_factor | 1.3206 |
| gross_win_rate | 0.5714 |
| sharpe_ratio | -0.0734 |
| sortino_ratio | -0.0175 |
| max_drawdown | 0.1122 |
| cagr | -0.0127 |
| net_avg_win | 84.6657 |
| net_avg_loss | -115.6514 |
| avg_hold_time_bars | 5.9474 |
| exposure | 0.0719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
