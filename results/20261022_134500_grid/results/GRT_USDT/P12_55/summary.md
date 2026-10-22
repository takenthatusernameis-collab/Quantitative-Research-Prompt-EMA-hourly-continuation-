# EMA Hourly Continuation — GRT/USDT P12_55

**Symbol:** GRT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 986 |
| net_profit_factor | 0.6248 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.9898 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -5.4852 |
| sortino_ratio | -2.4129 |
| max_drawdown | 0.9506 |
| cagr | -0.6908 |
| net_avg_win | 33.4578 |
| net_avg_loss | -49.1719 |
| avg_hold_time_bars | 8.5487 |
| exposure | 0.3814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
