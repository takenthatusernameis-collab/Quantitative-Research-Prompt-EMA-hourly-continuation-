# EMA Hourly Continuation — PEOPLE/USDT P34_89

**Symbol:** PEOPLE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 700 |
| net_profit_factor | 0.5955 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.8721 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -4.1525 |
| sortino_ratio | -1.5483 |
| max_drawdown | 0.8513 |
| cagr | -0.5187 |
| net_avg_win | 37.6744 |
| net_avg_loss | -56.1035 |
| avg_hold_time_bars | 7.6286 |
| exposure | 0.2416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
