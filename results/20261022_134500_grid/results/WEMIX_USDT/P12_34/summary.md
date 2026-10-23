# EMA Hourly Continuation — WEMIX/USDT P12_34

**Symbol:** WEMIX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1823 |
| net_profit_factor | 0.1864 |
| net_win_rate | 0.2968 |
| gross_profit_factor | 0.4357 |
| gross_win_rate | 0.3165 |
| sharpe_ratio | -19.5129 |
| sortino_ratio | -11.9982 |
| max_drawdown | 1.0000 |
| cagr | -0.9982 |
| net_avg_win | 4.2341 |
| net_avg_loss | -9.5871 |
| avg_hold_time_bars | 3.5096 |
| exposure | 0.2908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
