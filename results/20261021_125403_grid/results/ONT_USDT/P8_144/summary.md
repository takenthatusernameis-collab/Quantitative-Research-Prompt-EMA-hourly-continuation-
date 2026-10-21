# EMA Hourly Continuation — ONT/USDT P8_144

**Symbol:** ONT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.7368 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 0.8914 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -1.9511 |
| sortino_ratio | -0.5842 |
| max_drawdown | 0.5265 |
| cagr | -0.2363 |
| net_avg_win | 65.4726 |
| net_avg_loss | -80.1263 |
| avg_hold_time_bars | 34.0854 |
| exposure | 0.6864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
