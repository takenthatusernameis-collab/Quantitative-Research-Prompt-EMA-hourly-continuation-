# EMA Hourly Continuation — LUNA/USDT P89_100

**Symbol:** LUNA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.1917 |
| net_win_rate | 0.3418 |
| gross_profit_factor | 0.6424 |
| gross_win_rate | 0.3972 |
| sharpe_ratio | -11.7806 |
| sortino_ratio | -4.6160 |
| max_drawdown | 0.9981 |
| cagr | -0.9175 |
| net_avg_win | 9.8211 |
| net_avg_loss | -26.6119 |
| avg_hold_time_bars | 2.1418 |
| exposure | 0.0686 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
