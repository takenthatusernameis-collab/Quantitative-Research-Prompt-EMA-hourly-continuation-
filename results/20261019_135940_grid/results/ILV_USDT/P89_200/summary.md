# EMA Hourly Continuation — ILV/USDT P89_200

**Symbol:** ILV/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.6442 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9449 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -2.5205 |
| sortino_ratio | -0.6665 |
| max_drawdown | 0.5491 |
| cagr | -0.2706 |
| net_avg_win | 59.3353 |
| net_avg_loss | -84.5117 |
| avg_hold_time_bars | 14.0831 |
| exposure | 0.2234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
