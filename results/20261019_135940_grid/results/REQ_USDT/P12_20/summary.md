# EMA Hourly Continuation — REQ/USDT P12_20

**Symbol:** REQ/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1606 |
| net_profit_factor | 0.2754 |
| net_win_rate | 0.3431 |
| gross_profit_factor | 0.8693 |
| gross_win_rate | 0.4103 |
| sharpe_ratio | -18.0125 |
| sortino_ratio | -10.5949 |
| max_drawdown | 1.0000 |
| cagr | -0.9965 |
| net_avg_win | 6.8986 |
| net_avg_loss | -13.0816 |
| avg_hold_time_bars | 2.5685 |
| exposure | 0.1875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
