# EMA Hourly Continuation — MNT/USDT P20_200

**Symbol:** MNT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.9137 |
| net_win_rate | 0.5326 |
| gross_profit_factor | 1.1190 |
| gross_win_rate | 0.5326 |
| sharpe_ratio | -0.3904 |
| sortino_ratio | -0.0907 |
| max_drawdown | 0.1936 |
| cagr | -0.0442 |
| net_avg_win | 81.7600 |
| net_avg_loss | -101.9486 |
| avg_hold_time_bars | 57.1341 |
| exposure | 0.6778 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
