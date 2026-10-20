# EMA Hourly Continuation — KNC/USDT P12_55

**Symbol:** KNC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 862 |
| net_profit_factor | 0.5961 |
| net_win_rate | 0.4466 |
| gross_profit_factor | 0.9828 |
| gross_win_rate | 0.4675 |
| sharpe_ratio | -6.2410 |
| sortino_ratio | -2.5833 |
| max_drawdown | 0.9573 |
| cagr | -0.7122 |
| net_avg_win | 36.6533 |
| net_avg_loss | -49.6298 |
| avg_hold_time_bars | 11.2680 |
| exposure | 0.4415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
