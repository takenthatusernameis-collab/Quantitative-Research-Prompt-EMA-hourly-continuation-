# EMA Hourly Continuation — NYM/USDT P144_200

**Symbol:** NYM/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 170 |
| net_profit_factor | 0.3712 |
| net_win_rate | 0.3824 |
| gross_profit_factor | 0.5968 |
| gross_win_rate | 0.3824 |
| sharpe_ratio | -3.6462 |
| sortino_ratio | -0.6776 |
| max_drawdown | 0.5529 |
| cagr | -0.2742 |
| net_avg_win | 50.2076 |
| net_avg_loss | -83.7347 |
| avg_hold_time_bars | 12.7176 |
| exposure | 0.0983 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
