# EMA Hourly Continuation — IMX/USDT P20_144

**Symbol:** IMX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.6927 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 0.9841 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -2.2271 |
| sortino_ratio | -0.6938 |
| max_drawdown | 0.5914 |
| cagr | -0.2845 |
| net_avg_win | 51.6200 |
| net_avg_loss | -75.7405 |
| avg_hold_time_bars | 25.0364 |
| exposure | 0.5597 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
