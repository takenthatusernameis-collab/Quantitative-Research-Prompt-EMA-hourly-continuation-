# EMA Hourly Continuation — ADA/USDT P89_200

**Symbol:** ADA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.5627 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 1.0069 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -3.4424 |
| sortino_ratio | -0.9285 |
| max_drawdown | 0.6876 |
| cagr | -0.3663 |
| net_avg_win | 49.3012 |
| net_avg_loss | -79.9789 |
| avg_hold_time_bars | 11.2735 |
| exposure | 0.1911 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
