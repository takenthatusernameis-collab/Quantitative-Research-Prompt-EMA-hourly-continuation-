# EMA Hourly Continuation — LINK/USDT P20_89

**Symbol:** LINK/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.5780 |
| net_win_rate | 0.4548 |
| gross_profit_factor | 0.9301 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -5.1890 |
| sortino_ratio | -1.8849 |
| max_drawdown | 0.9056 |
| cagr | -0.6022 |
| net_avg_win | 40.2077 |
| net_avg_loss | -58.0332 |
| avg_hold_time_bars | 11.6726 |
| exposure | 0.3581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
