# EMA Hourly Continuation — MOVR/USDT P26_100

**Symbol:** MOVR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.5322 |
| net_win_rate | 0.4415 |
| gross_profit_factor | 0.8591 |
| gross_win_rate | 0.4584 |
| sharpe_ratio | -5.1042 |
| sortino_ratio | -1.9124 |
| max_drawdown | 0.9058 |
| cagr | -0.5976 |
| net_avg_win | 32.6494 |
| net_avg_loss | -48.4918 |
| avg_hold_time_bars | 10.2891 |
| exposure | 0.3316 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
