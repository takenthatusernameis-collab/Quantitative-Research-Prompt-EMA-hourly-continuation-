# EMA Hourly Continuation — XEC/USDT P12_200

**Symbol:** XEC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.8049 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 1.0121 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -1.3460 |
| sortino_ratio | -0.3813 |
| max_drawdown | 0.4261 |
| cagr | -0.1621 |
| net_avg_win | 74.6164 |
| net_avg_loss | -94.6071 |
| avg_hold_time_bars | 39.0609 |
| exposure | 0.6964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
