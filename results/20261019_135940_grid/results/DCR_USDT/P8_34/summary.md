# EMA Hourly Continuation — DCR/USDT P8_34

**Symbol:** DCR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1374 |
| net_profit_factor | 0.3910 |
| net_win_rate | 0.4214 |
| gross_profit_factor | 0.6928 |
| gross_win_rate | 0.4425 |
| sharpe_ratio | -9.4520 |
| sortino_ratio | -4.9295 |
| max_drawdown | 0.9979 |
| cagr | -0.9104 |
| net_avg_win | 11.0633 |
| net_avg_loss | -20.6074 |
| avg_hold_time_bars | 5.6295 |
| exposure | 0.3500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
