# EMA Hourly Continuation — ATH/USDT P8_26

**Symbol:** ATH/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1445 |
| net_profit_factor | 0.4821 |
| net_win_rate | 0.4567 |
| gross_profit_factor | 0.8412 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -8.7193 |
| sortino_ratio | -4.7921 |
| max_drawdown | 0.9965 |
| cagr | -0.9073 |
| net_avg_win | 14.0506 |
| net_avg_loss | -24.5051 |
| avg_hold_time_bars | 3.6886 |
| exposure | 0.2583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
