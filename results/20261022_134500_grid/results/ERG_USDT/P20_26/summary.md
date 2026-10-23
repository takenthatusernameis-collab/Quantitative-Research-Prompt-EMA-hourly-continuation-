# EMA Hourly Continuation — ERG/USDT P20_26

**Symbol:** ERG/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1232 |
| net_profit_factor | 0.1268 |
| net_win_rate | 0.2622 |
| gross_profit_factor | 0.3868 |
| gross_win_rate | 0.3060 |
| sharpe_ratio | -18.1651 |
| sortino_ratio | -9.5654 |
| max_drawdown | 1.0000 |
| cagr | -0.9940 |
| net_avg_win | 4.4940 |
| net_avg_loss | -12.5980 |
| avg_hold_time_bars | 2.1599 |
| exposure | 0.1210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
