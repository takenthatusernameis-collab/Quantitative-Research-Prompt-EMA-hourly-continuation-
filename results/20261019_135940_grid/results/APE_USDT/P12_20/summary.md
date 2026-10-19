# EMA Hourly Continuation — APE/USDT P12_20

**Symbol:** APE/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1462 |
| net_profit_factor | 0.2602 |
| net_win_rate | 0.3899 |
| gross_profit_factor | 0.7104 |
| gross_win_rate | 0.4186 |
| sharpe_ratio | -13.7317 |
| sortino_ratio | -7.5108 |
| max_drawdown | 0.9999 |
| cagr | -0.9786 |
| net_avg_win | 6.1697 |
| net_avg_loss | -15.1526 |
| avg_hold_time_bars | 2.0363 |
| exposure | 0.1353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
