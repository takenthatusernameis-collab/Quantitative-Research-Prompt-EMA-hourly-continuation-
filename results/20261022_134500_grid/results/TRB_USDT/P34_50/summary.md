# EMA Hourly Continuation — TRB/USDT P34_50

**Symbol:** TRB/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1021 |
| net_profit_factor | 0.3635 |
| net_win_rate | 0.3830 |
| gross_profit_factor | 0.7496 |
| gross_win_rate | 0.4172 |
| sharpe_ratio | -11.4554 |
| sortino_ratio | -5.2647 |
| max_drawdown | 0.9988 |
| cagr | -0.9295 |
| net_avg_win | 14.5848 |
| net_avg_loss | -24.9052 |
| avg_hold_time_bars | 2.4310 |
| exposure | 0.1123 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
