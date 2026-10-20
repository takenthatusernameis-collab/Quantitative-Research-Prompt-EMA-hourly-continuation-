# EMA Hourly Continuation — TRB/USDT P8_26

**Symbol:** TRB/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1604 |
| net_profit_factor | 0.4300 |
| net_win_rate | 0.4165 |
| gross_profit_factor | 0.8875 |
| gross_win_rate | 0.4408 |
| sharpe_ratio | -11.6360 |
| sortino_ratio | -6.5499 |
| max_drawdown | 0.9998 |
| cagr | -0.9628 |
| net_avg_win | 11.2903 |
| net_avg_loss | -18.7387 |
| avg_hold_time_bars | 4.0031 |
| exposure | 0.2906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
