# EMA Hourly Continuation — CRO/USDT P50_55

**Symbol:** CRO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 821 |
| net_profit_factor | 0.1324 |
| net_win_rate | 0.2826 |
| gross_profit_factor | 0.5913 |
| gross_win_rate | 0.3739 |
| sharpe_ratio | -15.0234 |
| sortino_ratio | -6.6692 |
| max_drawdown | 0.9999 |
| cagr | -0.9760 |
| net_avg_win | 6.5751 |
| net_avg_loss | -19.5663 |
| avg_hold_time_bars | 2.0597 |
| exposure | 0.0769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
