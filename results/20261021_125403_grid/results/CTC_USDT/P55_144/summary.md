# EMA Hourly Continuation — CTC/USDT P55_144

**Symbol:** CTC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.7862 |
| net_win_rate | 0.5111 |
| gross_profit_factor | 1.0407 |
| gross_win_rate | 0.5111 |
| sharpe_ratio | -1.4201 |
| sortino_ratio | -0.3868 |
| max_drawdown | 0.4072 |
| cagr | -0.1637 |
| net_avg_win | 72.2702 |
| net_avg_loss | -96.1018 |
| avg_hold_time_bars | 14.6722 |
| exposure | 0.2401 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
