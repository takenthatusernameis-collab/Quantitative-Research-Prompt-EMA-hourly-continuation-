# EMA Hourly Continuation — QNT/USDT P12_144

**Symbol:** QNT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.8300 |
| net_win_rate | 0.5106 |
| gross_profit_factor | 1.0470 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -1.3868 |
| sortino_ratio | -0.4528 |
| max_drawdown | 0.4724 |
| cagr | -0.1893 |
| net_avg_win | 75.7718 |
| net_avg_loss | -95.2582 |
| avg_hold_time_bars | 24.3907 |
| exposure | 0.5732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
