# EMA Hourly Continuation — INJ/USDT P12_200

**Symbol:** INJ/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.5991 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.8134 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -2.8836 |
| sortino_ratio | -0.7149 |
| max_drawdown | 0.5990 |
| cagr | -0.2926 |
| net_avg_win | 62.0034 |
| net_avg_loss | -81.8547 |
| avg_hold_time_bars | 54.0473 |
| exposure | 0.7788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
