# EMA Hourly Continuation — AMP/USDT P20_100

**Symbol:** AMP/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 976 |
| net_profit_factor | 0.3973 |
| net_win_rate | 0.3770 |
| gross_profit_factor | 0.6970 |
| gross_win_rate | 0.3904 |
| sharpe_ratio | -9.5420 |
| sortino_ratio | -4.1857 |
| max_drawdown | 0.9951 |
| cagr | -0.8760 |
| net_avg_win | 17.8220 |
| net_avg_loss | -27.1474 |
| avg_hold_time_bars | 9.7295 |
| exposure | 0.4316 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
