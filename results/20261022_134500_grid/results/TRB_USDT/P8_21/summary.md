# EMA Hourly Continuation — TRB/USDT P8_21

**Symbol:** TRB/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1742 |
| net_profit_factor | 0.3426 |
| net_win_rate | 0.4087 |
| gross_profit_factor | 0.7317 |
| gross_win_rate | 0.4357 |
| sharpe_ratio | -13.0768 |
| sortino_ratio | -7.7255 |
| max_drawdown | 0.9999 |
| cagr | -0.9793 |
| net_avg_win | 7.3190 |
| net_avg_loss | -14.7675 |
| avg_hold_time_bars | 3.0821 |
| exposure | 0.2430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
