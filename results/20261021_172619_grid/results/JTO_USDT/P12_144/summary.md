# EMA Hourly Continuation — JTO/USDT P12_144

**Symbol:** JTO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.8554 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 0.9901 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -0.9371 |
| sortino_ratio | -0.2685 |
| max_drawdown | 0.3388 |
| cagr | -0.1188 |
| net_avg_win | 80.4696 |
| net_avg_loss | -93.6022 |
| avg_hold_time_bars | 35.9726 |
| exposure | 0.6557 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
