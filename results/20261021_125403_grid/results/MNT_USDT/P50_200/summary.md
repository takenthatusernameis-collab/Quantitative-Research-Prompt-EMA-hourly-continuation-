# EMA Hourly Continuation — MNT/USDT P50_200

**Symbol:** MNT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 218 |
| net_profit_factor | 0.6956 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.8827 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -1.4936 |
| sortino_ratio | -0.3139 |
| max_drawdown | 0.3519 |
| cagr | -0.1355 |
| net_avg_win | 67.3209 |
| net_avg_loss | -88.2866 |
| avg_hold_time_bars | 48.8303 |
| exposure | 0.4839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
