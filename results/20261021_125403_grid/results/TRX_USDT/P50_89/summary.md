# EMA Hourly Continuation — TRX/USDT P50_89

**Symbol:** TRX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.3904 |
| net_win_rate | 0.4552 |
| gross_profit_factor | 0.9611 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -4.6302 |
| sortino_ratio | -1.1199 |
| max_drawdown | 0.7265 |
| cagr | -0.4017 |
| net_avg_win | 38.0449 |
| net_avg_loss | -81.4324 |
| avg_hold_time_bars | 8.6866 |
| exposure | 0.1058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
