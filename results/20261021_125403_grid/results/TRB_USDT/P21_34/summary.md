# EMA Hourly Continuation — TRB/USDT P21_34

**Symbol:** TRB/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.5499 |
| net_win_rate | 0.4260 |
| gross_profit_factor | 0.7745 |
| gross_win_rate | 0.4260 |
| sharpe_ratio | -3.6874 |
| sortino_ratio | -0.9540 |
| max_drawdown | 0.6699 |
| cagr | -0.3554 |
| net_avg_win | 58.0179 |
| net_avg_loss | -78.3015 |
| avg_hold_time_bars | 5.2205 |
| exposure | 0.0782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
