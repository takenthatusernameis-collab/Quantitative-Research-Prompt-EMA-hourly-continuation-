# EMA Hourly Continuation — BAND/USDT P20_89

**Symbol:** BAND/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.7245 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9429 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -2.6281 |
| sortino_ratio | -0.8638 |
| max_drawdown | 0.6563 |
| cagr | -0.3283 |
| net_avg_win | 65.3406 |
| net_avg_loss | -82.1330 |
| avg_hold_time_bars | 16.0467 |
| exposure | 0.3885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
