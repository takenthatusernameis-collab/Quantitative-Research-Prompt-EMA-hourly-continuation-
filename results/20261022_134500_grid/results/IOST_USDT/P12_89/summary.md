# EMA Hourly Continuation — IOST/USDT P12_89

**Symbol:** IOST/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.6748 |
| net_win_rate | 0.5082 |
| gross_profit_factor | 1.0693 |
| gross_win_rate | 0.5196 |
| sharpe_ratio | -2.9628 |
| sortino_ratio | -1.0355 |
| max_drawdown | 0.7160 |
| cagr | -0.3890 |
| net_avg_win | 47.3712 |
| net_avg_loss | -72.5286 |
| avg_hold_time_bars | 21.5686 |
| exposure | 0.6000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
