# EMA Hourly Continuation — SQD/USDT P12_144

**Symbol:** SQD/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.7936 |
| net_win_rate | 0.5064 |
| gross_profit_factor | 1.0203 |
| gross_win_rate | 0.5083 |
| sharpe_ratio | -1.6385 |
| sortino_ratio | -0.5529 |
| max_drawdown | 0.5144 |
| cagr | -0.2286 |
| net_avg_win | 65.3568 |
| net_avg_loss | -84.5082 |
| avg_hold_time_bars | 23.8748 |
| exposure | 0.6094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
