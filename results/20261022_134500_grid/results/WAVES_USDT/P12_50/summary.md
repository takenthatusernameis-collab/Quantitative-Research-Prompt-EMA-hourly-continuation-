# EMA Hourly Continuation — WAVES/USDT P12_50

**Symbol:** WAVES/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1243 |
| net_profit_factor | 0.4841 |
| net_win_rate | 0.4320 |
| gross_profit_factor | 0.9448 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -9.2989 |
| sortino_ratio | -4.6114 |
| max_drawdown | 0.9970 |
| cagr | -0.8999 |
| net_avg_win | 17.4227 |
| net_avg_loss | -27.3726 |
| avg_hold_time_bars | 6.2132 |
| exposure | 0.3510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
