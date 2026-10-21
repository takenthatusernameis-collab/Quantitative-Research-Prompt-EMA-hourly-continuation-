# EMA Hourly Continuation — JASMY/USDT P26_89

**Symbol:** JASMY/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.8203 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 1.0188 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -1.2866 |
| sortino_ratio | -0.3880 |
| max_drawdown | 0.4131 |
| cagr | -0.1650 |
| net_avg_win | 74.2180 |
| net_avg_loss | -92.9701 |
| avg_hold_time_bars | 13.6652 |
| exposure | 0.2745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
