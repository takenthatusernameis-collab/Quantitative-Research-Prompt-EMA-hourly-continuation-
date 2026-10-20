# EMA Hourly Continuation — NMR/USDT P12_55

**Symbol:** NMR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1065 |
| net_profit_factor | 0.6326 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 1.0116 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -6.3743 |
| sortino_ratio | -2.9307 |
| max_drawdown | 0.9729 |
| cagr | -0.7563 |
| net_avg_win | 33.7846 |
| net_avg_loss | -46.3767 |
| avg_hold_time_bars | 7.8845 |
| exposure | 0.3817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
