# EMA Hourly Continuation — REQ/USDT P8_26

**Symbol:** REQ/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 757 |
| net_profit_factor | 0.5405 |
| net_win_rate | 0.4240 |
| gross_profit_factor | 0.8431 |
| gross_win_rate | 0.4254 |
| sharpe_ratio | -6.8016 |
| sortino_ratio | -2.6822 |
| max_drawdown | 0.9576 |
| cagr | -0.7144 |
| net_avg_win | 35.0653 |
| net_avg_loss | -47.7667 |
| avg_hold_time_bars | 6.9841 |
| exposure | 0.2403 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
