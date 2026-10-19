# EMA Hourly Continuation — MNT/USDT P144_200

**Symbol:** MNT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.4308 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8517 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -4.0592 |
| sortino_ratio | -1.0670 |
| max_drawdown | 0.7425 |
| cagr | -0.4034 |
| net_avg_win | 34.1693 |
| net_avg_loss | -69.3941 |
| avg_hold_time_bars | 5.8406 |
| exposure | 0.0916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
