# EMA Hourly Continuation — SHIB/USDT P12_20

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1479 |
| net_profit_factor | 0.2233 |
| net_win_rate | 0.3874 |
| gross_profit_factor | 0.7467 |
| gross_win_rate | 0.4388 |
| sharpe_ratio | -15.3536 |
| sortino_ratio | -8.5358 |
| max_drawdown | 1.0000 |
| cagr | -0.9898 |
| net_avg_win | 5.0182 |
| net_avg_loss | -14.2112 |
| avg_hold_time_bars | 2.0135 |
| exposure | 0.1354 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
