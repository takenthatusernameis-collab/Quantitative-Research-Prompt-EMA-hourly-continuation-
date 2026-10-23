# EMA Hourly Continuation — CATI/USDT P8_89

**Symbol:** CATI/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.5467 |
| net_win_rate | 0.4312 |
| gross_profit_factor | 0.8496 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -5.6858 |
| sortino_ratio | -2.0484 |
| max_drawdown | 0.8871 |
| cagr | -0.6358 |
| net_avg_win | 44.4962 |
| net_avg_loss | -61.6863 |
| avg_hold_time_bars | 22.2029 |
| exposure | 0.6718 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
