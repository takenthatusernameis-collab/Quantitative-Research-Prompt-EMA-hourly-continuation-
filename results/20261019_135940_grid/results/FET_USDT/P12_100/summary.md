# EMA Hourly Continuation — FET/USDT P12_100

**Symbol:** FET/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.6843 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9338 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -2.8271 |
| sortino_ratio | -0.9215 |
| max_drawdown | 0.6911 |
| cagr | -0.3595 |
| net_avg_win | 55.9175 |
| net_avg_loss | -75.6324 |
| avg_hold_time_bars | 25.5083 |
| exposure | 0.6296 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
