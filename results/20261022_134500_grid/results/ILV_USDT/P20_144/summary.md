# EMA Hourly Continuation — ILV/USDT P20_144

**Symbol:** ILV/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.6990 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 1.0058 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -2.5025 |
| sortino_ratio | -0.8148 |
| max_drawdown | 0.6282 |
| cagr | -0.3188 |
| net_avg_win | 55.2472 |
| net_avg_loss | -76.3984 |
| avg_hold_time_bars | 22.2873 |
| exposure | 0.5359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
