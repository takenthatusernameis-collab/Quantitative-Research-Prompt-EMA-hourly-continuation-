# EMA Hourly Continuation — ILV/USDT P144_200

**Symbol:** ILV/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 208 |
| net_profit_factor | 0.9100 |
| net_win_rate | 0.5529 |
| gross_profit_factor | 1.2320 |
| gross_win_rate | 0.5529 |
| sharpe_ratio | -0.3684 |
| sortino_ratio | -0.0772 |
| max_drawdown | 0.1788 |
| cagr | -0.0370 |
| net_avg_win | 79.4081 |
| net_avg_loss | -107.9071 |
| avg_hold_time_bars | 7.5529 |
| exposure | 0.0714 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
