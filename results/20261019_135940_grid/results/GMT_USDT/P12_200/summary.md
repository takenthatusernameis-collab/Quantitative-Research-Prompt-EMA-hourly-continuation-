# EMA Hourly Continuation — GMT/USDT P12_200

**Symbol:** GMT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.7889 |
| net_win_rate | 0.5275 |
| gross_profit_factor | 1.1407 |
| gross_win_rate | 0.5372 |
| sharpe_ratio | -1.1936 |
| sortino_ratio | -0.2953 |
| max_drawdown | 0.3520 |
| cagr | -0.1333 |
| net_avg_win | 69.2160 |
| net_avg_loss | -97.9535 |
| avg_hold_time_bars | 55.9223 |
| exposure | 0.7855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
