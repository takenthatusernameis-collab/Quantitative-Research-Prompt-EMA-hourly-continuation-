# EMA Hourly Continuation — ATOM/USDT P12_89

**Symbol:** ATOM/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.6237 |
| net_win_rate | 0.4892 |
| gross_profit_factor | 0.9852 |
| gross_win_rate | 0.4907 |
| sharpe_ratio | -4.0496 |
| sortino_ratio | -1.4969 |
| max_drawdown | 0.8527 |
| cagr | -0.5181 |
| net_avg_win | 40.8390 |
| net_avg_loss | -62.7167 |
| avg_hold_time_bars | 16.6973 |
| exposure | 0.5290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
